from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List
import uuid
from datetime import datetime, timezone

from models import ContactMessage, ContactMessageDB, ContactResponse
from cv_generator import CVGenerator


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


# Define Models
class StatusCheck(BaseModel):
    model_config = ConfigDict(extra="ignore")  # Ignore MongoDB's _id field
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class StatusCheckCreate(BaseModel):
    client_name: str

# Add your routes to the router instead of directly to app
@api_router.get("/")
async def root():
    return {"message": "Hello World"}

@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_dict = input.model_dump()
    status_obj = StatusCheck(**status_dict)
    
    # Convert to dict and serialize datetime to ISO string for MongoDB
    doc = status_obj.model_dump()
    doc['timestamp'] = doc['timestamp'].isoformat()
    
    _ = await db.status_checks.insert_one(doc)
    return status_obj

@api_router.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    # Exclude MongoDB's _id field from the query results
    status_checks = await db.status_checks.find({}, {"_id": 0}).to_list(1000)
    
    # Convert ISO string timestamps back to datetime objects
    for check in status_checks:
        if isinstance(check['timestamp'], str):
            check['timestamp'] = datetime.fromisoformat(check['timestamp'])
    
    return status_checks

# Contact form endpoint
@api_router.post("/contact", response_model=ContactResponse)
async def submit_contact(contact: ContactMessage):
    try:
        # Create DB model with timestamp and read status
        contact_db = ContactMessageDB(**contact.dict())
        
        # Insert into MongoDB
        result = await db.contact_messages.insert_one(contact_db.dict())
        
        return ContactResponse(
            success=True,
            message="Message envoyé avec succès",
            id=str(result.inserted_id)
        )
    except Exception as e:
        logging.error(f"Error saving contact message: {str(e)}")
        raise HTTPException(status_code=500, detail="Erreur lors de l'envoi du message")

# Download CV endpoint
@api_router.get("/download-cv")
async def download_cv():
    try:
        # Path to the CV PDF file
        cv_path = ROOT_DIR / "CV_Ali_Mansouri.pdf"
        
        if not cv_path.exists():
            raise HTTPException(status_code=404, detail="CV non trouvé")
        
        # Read the PDF file
        with open(cv_path, "rb") as pdf_file:
            pdf_content = pdf_file.read()
        
        # Return as streaming response
        from io import BytesIO
        pdf_buffer = BytesIO(pdf_content)
        
        return StreamingResponse(
            pdf_buffer,
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=CV_Ali_Mansouri.pdf"
            }
        )
    except Exception as e:
        logging.error(f"Error serving CV PDF: {str(e)}")
        raise HTTPException(status_code=500, detail="Erreur lors du téléchargement du PDF")

# Get all contact messages (admin endpoint)
@api_router.get("/contact-messages")
async def get_contact_messages():
    try:
        messages = await db.contact_messages.find().sort("created_at", -1).to_list(100)
        # Convert ObjectId to string for JSON serialization
        for msg in messages:
            msg['_id'] = str(msg['_id'])
        return messages
    except Exception as e:
        logging.error(f"Error fetching contact messages: {str(e)}")
        raise HTTPException(status_code=500, detail="Erreur lors de la récupération des messages")

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()