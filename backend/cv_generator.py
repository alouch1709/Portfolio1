from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
from portfolio_data import portfolio_data
import logging

logger = logging.getLogger(__name__)

class CVGenerator:
    def __init__(self):
        self.data = portfolio_data
        self.buffer = BytesIO()
        self.styles = getSampleStyleSheet()
        self._setup_styles()

    def _setup_styles(self):
        """Setup custom styles for the PDF"""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1C3FAA'),
            spaceAfter=12,
            alignment=TA_CENTER
        ))
        
        # Subtitle style
        self.styles.add(ParagraphStyle(
            name='Subtitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#374151'),
            spaceAfter=8,
            alignment=TA_CENTER
        ))
        
        # Section header
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#1C3FAA'),
            spaceAfter=10,
            spaceBefore=15,
            borderWidth=0,
            borderPadding=0,
            borderColor=colors.HexColor('#1C3FAA'),
            borderRadius=None
        ))
        
        # Job title style
        self.styles.add(ParagraphStyle(
            name='JobTitle',
            parent=self.styles['Heading3'],
            fontSize=12,
            textColor=colors.HexColor('#1C3FAA'),
            spaceAfter=4
        ))
        
        # Body text
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['BodyText'],
            fontSize=10,
            textColor=colors.HexColor('#374151'),
            spaceAfter=6
        ))

    def generate(self):
        """Generate the CV PDF"""
        try:
            doc = SimpleDocTemplate(
                self.buffer,
                pagesize=A4,
                rightMargin=50,
                leftMargin=50,
                topMargin=50,
                bottomMargin=50
            )
            
            story = []
            
            # Header
            story.extend(self._create_header())
            
            # Profile
            story.extend(self._create_profile())
            
            # Experience
            story.extend(self._create_experience())
            
            # Projects
            story.extend(self._create_projects())
            
            # Skills
            story.extend(self._create_skills())
            
            # Education
            story.extend(self._create_education())
            
            # Certifications
            story.extend(self._create_certifications())
            
            # Languages
            story.extend(self._create_languages())
            
            # Activities
            story.extend(self._create_activities())
            
            # Build PDF
            doc.build(story)
            self.buffer.seek(0)
            return self.buffer
            
        except Exception as e:
            logger.error(f"Error generating CV PDF: {str(e)}")
            raise

    def _create_header(self):
        """Create header section"""
        elements = []
        personal = self.data['personal']
        
        elements.append(Paragraph(personal['fullName'], self.styles['CustomTitle']))
        elements.append(Paragraph(personal['title'], self.styles['Subtitle']))
        
        contact_info = f"""
        <para align="center">
        {personal['email']} | {personal['phone']}<br/>
        {personal['location']}<br/>
        LinkedIn: {personal['linkedin']}<br/>
        GitHub: {personal['github']}
        </para>
        """
        elements.append(Paragraph(contact_info, self.styles['CustomBody']))
        elements.append(Spacer(1, 0.2*inch))
        
        return elements

    def _create_profile(self):
        """Create profile section"""
        elements = []
        elements.append(Paragraph("PROFIL PROFESSIONNEL", self.styles['SectionHeader']))
        elements.append(Paragraph(self.data['personal']['profile'], self.styles['CustomBody']))
        elements.append(Spacer(1, 0.2*inch))
        return elements

    def _create_experience(self):
        """Create experience section"""
        elements = []
        elements.append(Paragraph("EXPÉRIENCE PROFESSIONNELLE", self.styles['SectionHeader']))
        
        for exp in self.data['experience']:
            elements.append(Paragraph(exp['role'], self.styles['JobTitle']))
            company_info = f"<b>{exp['company']}</b> | {exp['location']} | {exp['startDate']} - {exp['endDate']}"
            elements.append(Paragraph(company_info, self.styles['CustomBody']))
            
            for resp in exp['responsibilities']:
                elements.append(Paragraph(f"• {resp}", self.styles['CustomBody']))
            
            elements.append(Spacer(1, 0.15*inch))
        
        return elements

    def _create_projects(self):
        """Create projects section"""
        elements = []
        elements.append(Paragraph("PROJETS", self.styles['SectionHeader']))
        
        for project in self.data['projects']:
            elements.append(Paragraph(f"<b>{project['name']}</b>", self.styles['JobTitle']))
            elements.append(Paragraph(project['description'], self.styles['CustomBody']))
            tools = ", ".join(project['tools'])
            elements.append(Paragraph(f"<i>Technologies: {tools}</i>", self.styles['CustomBody']))
            elements.append(Spacer(1, 0.1*inch))
        
        return elements

    def _create_skills(self):
        """Create skills section"""
        elements = []
        elements.append(Paragraph("COMPÉTENCES TECHNIQUES", self.styles['SectionHeader']))
        
        for category in self.data['skills'].values():
            title = category['title']
            items = ", ".join(category['items'])
            elements.append(Paragraph(f"<b>{title}:</b> {items}", self.styles['CustomBody']))
        
        elements.append(Spacer(1, 0.1*inch))
        return elements

    def _create_education(self):
        """Create education section"""
        elements = []
        elements.append(Paragraph("FORMATION", self.styles['SectionHeader']))
        
        for edu in self.data['education']:
            elements.append(Paragraph(f"<b>{edu['degree']}</b>", self.styles['JobTitle']))
            info = f"{edu['institution']} | {edu['startDate']} - {edu['endDate']}"
            elements.append(Paragraph(info, self.styles['CustomBody']))
            elements.append(Spacer(1, 0.1*inch))
        
        return elements

    def _create_certifications(self):
        """Create certifications section"""
        elements = []
        elements.append(Paragraph("CERTIFICATIONS", self.styles['SectionHeader']))
        
        for cert in self.data['certifications']:
            cert_text = f"• <b>{cert['name']}</b> - {cert['provider']} ({cert['status']})"
            elements.append(Paragraph(cert_text, self.styles['CustomBody']))
        
        elements.append(Spacer(1, 0.1*inch))
        return elements

    def _create_languages(self):
        """Create languages section"""
        elements = []
        elements.append(Paragraph("LANGUES", self.styles['SectionHeader']))
        
        for lang in self.data['languages']:
            lang_text = f"• <b>{lang['language']}</b>: {lang['level']}"
            elements.append(Paragraph(lang_text, self.styles['CustomBody']))
        
        elements.append(Spacer(1, 0.1*inch))
        return elements

    def _create_activities(self):
        """Create activities section"""
        elements = []
        elements.append(Paragraph("ENGAGEMENTS ASSOCIATIFS", self.styles['SectionHeader']))
        
        for activity in self.data['activities']:
            activity_text = f"• <b>{activity['organization']}</b> - {activity['role']} ({activity['period']})"
            elements.append(Paragraph(activity_text, self.styles['CustomBody']))
        
        return elements