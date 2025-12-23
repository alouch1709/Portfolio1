# Contrats API - Portfolio Ali Mansouri

## Architecture Backend

### Technologies
- **FastAPI**: Framework backend
- **MongoDB**: Base de données (Motor async driver)
- **ReportLab**: Génération de PDF pour le CV
- **CORS**: Configuré pour permettre les requêtes frontend

### Base de données MongoDB

#### Collection: `contact_messages`
```json
{
  "_id": "ObjectId",
  "name": "string",
  "email": "string",
  "subject": "string",
  "message": "string",
  "created_at": "datetime",
  "read": "boolean"
}
```

## Endpoints API

### 1. POST /api/contact
**Description**: Soumettre un message via le formulaire de contact

**Request Body**:
```json
{
  "name": "string (required)",
  "email": "string (required, email format)",
  "subject": "string (required)",
  "message": "string (required)"
}
```

**Response 200**:
```json
{
  "success": true,
  "message": "Message envoyé avec succès",
  "id": "message_id"
}
```

**Response 400**:
```json
{
  "detail": "Validation error message"
}
```

---

### 2. GET /api/download-cv
**Description**: Générer et télécharger le CV en PDF

**Query Parameters**: Aucun

**Response**: 
- **Content-Type**: `application/pdf`
- **Headers**: `Content-Disposition: attachment; filename=CV_Ali_Mansouri.pdf`
- **Body**: PDF file stream

**Response 500**:
```json
{
  "detail": "Erreur lors de la génération du PDF"
}
```

---

### 3. GET /api/contact-messages (Admin - optionnel)
**Description**: Récupérer tous les messages de contact

**Response 200**:
```json
[
  {
    "id": "string",
    "name": "string",
    "email": "string",
    "subject": "string",
    "message": "string",
    "created_at": "ISO datetime",
    "read": false
  }
]
```

## Intégration Frontend ↔ Backend

### Mock Data à Remplacer

#### Dans `Contact.jsx`:
**AVANT** (Mock):
```javascript
setTimeout(() => {
  toast({ title: "Message envoyé !", description: "..." });
  setFormData({ name: '', email: '', subject: '', message: '' });
  setIsSubmitting(false);
}, 1000);
```

**APRÈS** (Backend):
```javascript
const response = await axios.post(`${BACKEND_URL}/api/contact`, formData);
if (response.data.success) {
  toast({ title: "Message envoyé !", description: "..." });
  setFormData({ name: '', email: '', subject: '', message: '' });
}
```

---

#### Dans `Hero.jsx`:
**AVANT** (Mock):
```javascript
const handleDownloadCV = () => {
  alert('Fonctionnalité de téléchargement du CV à venir!');
};
```

**APRÈS** (Backend):
```javascript
const handleDownloadCV = async () => {
  window.open(`${BACKEND_URL}/api/download-cv`, '_blank');
};
```

## Génération PDF

### Structure du CV PDF
1. **En-tête**: Nom, titre, contact
2. **Profil**: Description professionnelle
3. **Expérience**: Liste chronologique avec détails
4. **Projets**: Projets principaux avec outils
5. **Compétences**: Catégories de compétences
6. **Formation**: Parcours académique
7. **Certifications**: Certifications en cours/obtenues
8. **Langues**: Langues parlées avec niveau
9. **Engagements**: Activités associatives

### Données pour le PDF
Les données seront importées depuis `/app/frontend/src/mockData.js` (structure identique) dans le backend Python sous forme de dictionnaire.

## Gestion des erreurs

### Frontend
- Afficher des messages d'erreur via toast
- Désactiver les boutons pendant les requêtes
- Gérer les timeouts réseau

### Backend
- Validation des données avec Pydantic
- Try/catch pour les opérations DB
- Logs détaillés des erreurs
- Messages d'erreur clairs

## Variables d'environnement

### Backend `.env`
```
MONGO_URL=mongodb://localhost:27017
DB_NAME=portfolio_db
```

### Frontend `.env`
```
REACT_APP_BACKEND_URL=http://localhost:8001
```

## Tests à effectuer

1. ✅ Soumettre le formulaire de contact
2. ✅ Vérifier l'enregistrement dans MongoDB
3. ✅ Télécharger le CV en PDF
4. ✅ Vérifier le contenu du PDF
5. ✅ Tester les validations (champs vides, email invalide)
6. ✅ Tester les erreurs réseau
7. ✅ Vérifier le mode sombre/clair
