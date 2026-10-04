"""
Internship Tracker - Web Scraper
Automatically scrapes job offers from financial institutions
"""

import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import hashlib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class JobScraper:
    def __init__(self, config_path='sites_config.json'):
        with open(config_path, 'r') as f:
            self.sites_config = json.load(f)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.scraped_offers = []
    
    def scrape_all(self):
        """Scrape all configured sites"""
        logger.info("Starting web scraping process...")
        
        for category, sites in self.sites_config.items():
            logger.info(f"Scraping category: {category}")
            for site in sites:
                self._scrape_site(site, category)
        
        return self.scraped_offers
    
    def _scrape_site(self, site, category):
        """Scrape individual site"""
        try:
            logger.info(f"Scraping {site['name']}...")
            response = requests.get(site['url'], headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Generic job card extraction
            job_cards = soup.find_all(['div', 'article'], {'class': ['job', 'position', 'offer', 'internship']})
            
            for card in job_cards:
                offer = self._extract_offer(card, site, category)
                if offer:
                    self.scraped_offers.append(offer)
        
        except Exception as e:
            logger.error(f"Error scraping {site['name']}: {str(e)}")
    
    def _extract_offer(self, card, site, category):
        """Extract job offer details from card"""
        try:
            # Extract text from card
            text = card.get_text()
            
            # Check if it's an internship
            if not any(kw in text.lower() for kw in ['internship', 'stage', 'traineeship', 'practicum']):
                return None
            
            # Create offer object
            offer_id = hashlib.md5(f"{site['name']}{text}".encode()).hexdigest()[:12]
            
            offer = {
                "id": offer_id,
                "company": site['name'],
                "category": category,
                "country": site['country'],
                "title": self._extract_title(card),
                "description": text[:500],
                "location": self._extract_location(card),
                "posted_date": datetime.now().isoformat(),
                "deadline": "Not specified",
                "link": site['url'],
                "application_steps": "To be determined",
                "status": "new"
            }
            
            return offer
        
        except Exception as e:
            logger.error(f"Error extracting offer: {str(e)}")
            return None
    
    def _extract_title(self, card):
        """Extract job title from card"""
        title_elem = card.find(['h2', 'h3', 'h4', 'strong'])
        if title_elem:
            return title_elem.get_text(strip=True)
        return "Internship Position"
    
    def _extract_location(self, card):
        """Extract location from card"""
        text = card.get_text()
        if 'lugano' in text.lower():
            return 'Lugano'
        elif 'milan' in text.lower() or 'milano' in text.lower():
            return 'Milano'
        elif 'zurich' in text.lower() or 'zurigo' in text.lower():
            return 'Zurich'
        return "Switzerland/Italy"
    
    def save_offers(self, output_path='../data/job_offers.json'):
        """Save scraped offers to JSON"""
        data = {
            "offers": self.scraped_offers,
            "last_updated": datetime.now().isoformat(),
            "total_count": len(self.scraped_offers)
        }
        
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"Saved {len(self.scraped_offers)} offers to {output_path}")

if __name__ == "__main__":
    scraper = JobScraper()
    offers = scraper.scrape_all()
    scraper.save_offers()
    print(f"✅ Scraping completed! Found {len(offers)} offers")
