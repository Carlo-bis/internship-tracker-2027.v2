"""
CV Personalizer - Automatically personalizes CV and Cover Letter for each job offer
"""

from docx import Document
from docx.shared import Pt
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CVPersonalizer:
    def __init__(self, cv_template_path='../data/CV_Template_Carlo.docx',
                 cl_template_path='../data/Cover_Letter_Template.docx'):
        self.cv_template = Document(cv_template_path)
        self.cl_template = Document(cl_template_path)
    
    def personalize_for_offer(self, offer, output_dir='../data/personalized'):
        """Personalize CV and cover letter for specific job offer"""
        try:
            # Extract key info from offer
            company = offer.get('company', 'Company')
            position = offer.get('title', 'Internship')
            industry = self._identify_industry(offer)
            
            logger.info(f"Personalizing for {company} - {position}")
            
            # Personalize cover letter
            self._personalize_cover_letter(company, position, industry)
            
            # Save documents
            cv_path = f"{output_dir}/{company}_{position}_CV.docx"
            cl_path = f"{output_dir}/{company}_{position}_Cover_Letter.docx"
            
            self.cv_template.save(cv_path)
            self.cl_template.save(cl_path)
            
            logger.info(f"Saved personalized documents for {company}")
            return {"cv": cv_path, "cover_letter": cl_path}
        
        except Exception as e:
            logger.error(f"Error personalizing documents: {str(e)}")
            return None
    
    def _personalize_cover_letter(self, company, position, industry):
        """Insert company and position specific text in cover letter"""
        for para in self.cl_template.paragraphs:
            if '[Company Name]' in para.text:
                para.text = para.text.replace('[Company Name]', company)
            if '[Position Title]' in para.text:
                para.text = para.text.replace('[Position Title]', position)
            if '[industry/role-specific context]' in para.text:
                para.text = para.text.replace('[industry/role-specific context]', industry)
    
    def _identify_industry(self, offer):
        """Identify industry from job offer"""
        category = offer.get('category', '')
        if 'vc_pe' in category:
            return 'venture capital and private equity'
        elif 'fintech' in category:
            return 'fintech and digital banking'
        elif 'family_office' in category:
            return 'wealth management and family office services'
        else:
            return 'financial services and digital innovation'

if __name__ == "__main__":
    personalizer = CVPersonalizer()
    logger.info("CV Personalizer module loaded successfully")
