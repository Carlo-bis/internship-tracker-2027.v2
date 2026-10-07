```python
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
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Repository root
# scraper.py is located in: backend/scraper.py
# Therefore parent.parent = internship-tracker-2027/
BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_PATH = BASE_DIR / "sites_config.json"
DATA_DIR = BASE_DIR / "data"
OUTPUT_PATH = DATA_DIR / "job_offers.json"


# ============================================================
# JOB SCRAPER
# ============================================================

class JobScraper:

    def __init__(self, config_path=CONFIG_PATH):

        logger.info("=" * 60)
        logger.info("Initializing Job Scraper")
        logger.info("=" * 60)

        logger.info(f"Repository root: {BASE_DIR}")
        logger.info(f"Config file: {config_path}")
        logger.info(f"Output file: {OUTPUT_PATH}")

        # Check that configuration exists
        if not Path(config_path).exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}"
            )

        # Load configuration
        with open(config_path, "r", encoding="utf-8") as f:
            self.sites_config = json.load(f)

        logger.info(
            f"Loaded configuration with "
            f"{len(self.sites_config)} categories"
        )

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,"
                "application/xml;q=0.9,image/avif,image/webp,"
                "*/*;q=0.8"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
        }

        self.scraped_offers = []


    # ========================================================
    # SCRAPE ALL SITES
    # ========================================================

    def scrape_all(self):

        logger.info("")
        logger.info("=" * 60)
        logger.info("STARTING WEB SCRAPING PROCESS")
        logger.info("=" * 60)

        for category, sites in self.sites_config.items():

            logger.info("")
            logger.info(f"Category: {category}")
            logger.info(f"Number of sites: {len(sites)}")

            for site in sites:
                self._scrape_site(site, category)

        logger.info("")
        logger.info("=" * 60)
        logger.info(
            f"SCRAPING COMPLETED - "
            f"{len(self.scraped_offers)} offers found"
        )
        logger.info("=" * 60)

        return self.scraped_offers


    # ========================================================
    # SCRAPE INDIVIDUAL SITE
    # ========================================================

    def _scrape_site(self, site, category):

        site_name = site.get("name", "Unknown site")
        site_url = site.get("url", "")

        try:

            logger.info("")
            logger.info("-" * 60)
            logger.info(f"Scraping: {site_name}")
            logger.info(f"URL: {site_url}")

            response = requests.get(
                site_url,
                headers=self.headers,
                timeout=30,
                allow_redirects=True
            )

            logger.info(f"HTTP status: {response.status_code}")
            logger.info(
                f"Response size: {len(response.content)} bytes"
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.content,
                "html.parser"
            )

            # Generic job card extraction
            job_cards = soup.find_all(
                ["div", "article"],
                {
                    "class": [
                        "job",
                        "position",
                        "offer",
                        "internship"
                    ]
                }
            )

            logger.info(
                f"Potential job cards found: {len(job_cards)}"
            )

            for card in job_cards:

                offer = self._extract_offer(
                    card,
                    site,
                    category
                )

                if offer:
                    self.scraped_offers.append(offer)

            logger.info(
                f"Offers extracted from {site_name}: "
                f"{len([o for o in self.scraped_offers if o['company'] == site_name])}"
            )

        except requests.exceptions.HTTPError as e:

            logger.error(
                f"HTTP error while scraping {site_name}: {e}"
            )

        except requests.exceptions.Timeout:

            logger.error(
                f"Timeout while scraping {site_name}"
            )

        except requests.exceptions.RequestException as e:

            logger.error(
                f"Request error while scraping "
                f"{site_name}: {e}"
            )

        except Exception as e:

            logger.exception(
                f"Unexpected error while scraping "
                f"{site_name}: {e}"
            )


    # ========================================================
    # EXTRACT OFFER
    # ========================================================

    def _extract_offer(self, card, site, category):

        try:

            # Extract all text from job card
            text = card.get_text(
                separator=" ",
                strip=True
            )

            # Internship-related keywords
            internship_keywords = [
                "intern",
                "internship",
                "stage",
                "stagiaire",
                "traineeship",
                "practicum",
                "off-cycle",
                "summer analyst",
                "summer internship",
                "graduate program",
                "analyst program",
                "working student",
                "student"
            ]

            # Check whether this appears to be an internship
            if not any(
                keyword in text.lower()
                for keyword in internship_keywords
            ):
                return None

            # Create unique ID
            offer_id = hashlib.md5(
                f"{site['name']}{text}".encode("utf-8")
            ).hexdigest()[:12]

            offer = {
                "id": offer_id,
                "company": site.get(
                    "name",
                    "Unknown company"
                ),
                "category": category,
                "country": site.get(
                    "country",
                    "Unknown"
                ),
                "title": self._extract_title(card),
                "description": text[:500],
                "location": self._extract_location(card),
                "posted_date": datetime.now().isoformat(),
                "deadline": "Not specified",
                "link": site.get("url", ""),
                "application_steps": "To be determined",
                "status": "new"
            }

            return offer

        except Exception as e:

            logger.error(
                f"Error extracting offer: {e}"
            )

            return None


    # ========================================================
    # EXTRACT TITLE
    # ========================================================

    def _extract_title(self, card):

        title_elem = card.find(
            ["h1", "h2", "h3", "h4", "strong"]
        )

        if title_elem:

            title = title_elem.get_text(
                strip=True
            )

            if title:
                return title

        return "Internship Position"


    # ========================================================
    # EXTRACT LOCATION
    # ========================================================

    def _extract_location(self, card):

        text = card.get_text(
            separator=" ",
            strip=True
        )

        text_lower = text.lower()

        if "lugano" in text_lower:
            return "Lugano"

        elif (
            "milan" in text_lower
            or "milano" in text_lower
        ):
            return "Milano"

        elif (
            "zurich" in text_lower
            or "zurigo" in text_lower
        ):
            return "Zurich"

        elif "geneva" in text_lower:
            return "Geneva"

        elif "geneve" in text_lower:
            return "Geneva"

        elif "rome" in text_lower:
            return "Rome"

        elif "venice" in text_lower:
            return "Venice"

        elif "london" in text_lower:
            return "London"

        elif "frankfurt" in text_lower:
            return "Frankfurt"

        elif "paris" in text_lower:
            return "Paris"

        return "Switzerland/Italy"


    # ========================================================
    # SAVE OFFERS
    # ========================================================

    def save_offers(self, output_path=OUTPUT_PATH):

        try:

            # Make sure data directory exists
            DATA_DIR.mkdir(
                parents=True,
                exist_ok=True
            )

            data = {
                "offers": self.scraped_offers,
                "last_updated": datetime.now().isoformat(),
                "total_count": len(self.scraped_offers)
            }

            with open(
                output_path,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    data,
                    f,
                    indent=2,
                    ensure_ascii=False
                )

            logger.info("")
            logger.info("=" * 60)
            logger.info("DATA SAVED SUCCESSFULLY")
            logger.info("=" * 60)
            logger.info(f"Output file: {output_path}")
            logger.info(
                f"Total offers: {len(self.scraped_offers)}"
            )
            logger.info("=" * 60)

        except Exception as e:

            logger.exception(
                f"Error saving offers: {e}"
            )

            raise


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    try:

        logger.info("")
        logger.info("🚀 Internship Tracker starting...")
        logger.info("")

        scraper = JobScraper()

        offers = scraper.scrape_all()

        scraper.save_offers()

        print("")
        print("=" * 60)
        print(
            f"✅ Scraping completed! "
            f"Found {len(offers)} offers"
        )
        print("=" * 60)
        print("")

    except Exception as e:

        logger.exception(
            f"❌ Scraper failed: {e}"
        )

        # Important for GitHub Actions:
        # exit with error code if something goes wrong
        raise
```
