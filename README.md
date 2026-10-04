# 🚀 Internship Tracker 2027

Automated platform to track and manage summer internship applications in finance across Switzerland and Italy.

**Built for:** Carlo Bisaglia | Finance | Digital Finance Track | USI Lugano  
**Target Markets:** Switzerland (Lugano) & Milano  
**Position Type:** 3-month summer internship  
**Focus:** Fintech, Digital Banking, Venture Capital, Family Offices

---

## ✨ Features

✅ **Automated Daily Scraping** - Monitors 30+ official career pages every 24 hours  
✅ **Modern React Dashboard** - Real-time filtering, searching, and application tracking  
✅ **CV Personalization** - Auto-generates personalized CV & cover letters for each role  
✅ **Full-Stack Automation** - GitHub Actions + Python backend + React frontend  
✅ **Always-On Deployment** - GitHub Pages + GitHub Actions  
✅ **Smart Filtering** - Filter by location, company, industry, application status  

---

## 📊 What It Monitors

### 🇨🇭 Swiss Organizations
- **Banks:** UBS, Raiffeisen, BNY Mellon, Vontobel, EFG, Cornèr Banca
- **VC/PE:** InnoSource Ventures, LGT Capital Partners
- **Family Offices:** Brightside Capital, LFG, Custodia, Fortitude Wealth
- **FinTech:** Revolut, DXT Commodities, Thire

### 🇮🇹 Italian Organizations  
- **Banks:** Intesa Sanpaolo, UniCredit, Mediobanca, Generali

**Total:** 30+ organizations scraped daily

---

## 🏗️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | React 18 + Vite + TailwindCSS |
| Backend | Python 3.11 + BeautifulSoup + Requests |
| Automation | GitHub Actions (Cron jobs) |
| Hosting | GitHub Pages (frontend) + GitHub (data) |
| Database | JSON (git-friendly, version-controlled) |
| Documents | python-docx (CV personalization) |

---

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/[YOUR-USERNAME]/internship-tracker-2027.git
cd internship-tracker-2027
```

### 2. Setup Python Backend

```bash
cd backend
pip install -r requirements.txt
```

### 3. Setup React Frontend

```bash
cd ../frontend
npm install
```

### 4. Add Your CV Templates

Save to `/data/`:
- `CV_Template_Carlo.docx` - Your base CV
- `Cover_Letter_Template.docx` - Your base cover letter

### 5. Test the Scraper

```bash
cd backend
python scraper.py
```

Should create/update `data/job_offers.json` with found opportunities.

### 6. Run Dashboard Locally

```bash
cd frontend
npm run dev
```

Open http://localhost:5173

---

## 📁 Project Structure

```
internship-tracker-2027/
│
├── backend/
│   ├── scraper.py              # Main scraping engine
│   ├── cv_personalizer.py      # Document personalization
│   ├── requirements.txt        # Python deps
│   └── sites_config.json       # 30+ monitored sites
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── JobList.jsx
│   │   │   ├── JobCard.jsx
│   │   │   ├── Filters.jsx
│   │   │   └── Stats.jsx
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── index.css
│   ├── public/index.html
│   ├── package.json
│   └── vite.config.js
│
├── data/
│   ├── job_offers.json         # Scraped opportunities (auto-updated)
│   ├── applications.json       # Your application tracking
│   ├── CV_Template_Carlo.docx
│   └── Cover_Letter_Template.docx
│
├── .github/workflows/
│   └── daily_scrape.yml        # GitHub Actions automation
│
├── .gitignore
├── LICENSE (MIT)
└── README.md
```

---

## ⚙️ How It Works

### Automated Daily Workflow

**6:00 AM UTC (7:00 CET)** - GitHub Actions triggers:

1. **Scrape** → Python visits all 30+ career pages
2. **Extract** → Job titles, companies, links, deadlines
3. **Deduplicate** → Remove duplicate postings
4. **Save** → Update `data/job_offers.json`
5. **Git Commit** → Push changes to GitHub
6. **Build** → React app built from latest data
7. **Deploy** → Deployed to GitHub Pages automatically

### Manual Workflow

```bash
# Run scraper manually
cd backend
python scraper.py

# Test personalization
python cv_personalizer.py

# Build and test frontend
cd ../frontend
npm run build
npm run preview
```

---

## 📝 Configuration

### Adding New Organizations

Edit `backend/sites_config.json`:

```json
{
  "category_name": [
    {
      "name": "Company Name",
      "url": "https://careers.example.com",
      "internship_path": "/internships",
      "country": "Switzerland"
    }
  ]
}
```

### Changing Scrape Schedule

Edit `.github/workflows/daily_scrape.yml`:

```yaml
schedule:
  - cron: '0 6 * * *'  # Every day at 6 AM UTC
  # Alternative patterns:
  # '0 */6 * * *'      # Every 6 hours
  # '0 9 * * 1-5'      # Weekdays at 9 AM
```

---

## 🎯 Usage Guide

### Dashboard Features

1. **Real-time Stats**
   - Total opportunities
   - Applications submitted
   - Success rate

2. **Smart Filtering**
   - By company name
   - By location
   - By industry/category
   - By application status

3. **Job Cards**
   - Quick overview of posting
   - Posted date & deadline
   - Application steps info
   - Links to original posting
   - "Mark as Applied" button
   - Download personalized CV button

4. **Tracking**
   - Track application status (new/applied/rejected/offer)
   - View application timeline
   - Notes and follow-ups

### Workflow Tips

✅ Update CV templates as your profile grows  
✅ Mark applications to track progress  
✅ Use filters to focus on specific sectors  
✅ Download personalized documents before applying  
✅ Track interview dates and feedback  
✅ Export data from JSON files for analysis  

---

## 🔧 Troubleshooting

### Scraper not finding opportunities

```bash
# Verbose mode
python backend/scraper.py -v

# Check site accessibility
curl https://careers.company.com

# Verify sites_config.json syntax
python -m json.tool backend/sites_config.json
```

### GitHub Actions failing

1. Check workflow logs: Repository → Actions → Daily Scraping
2. Verify Python dependencies: `pip list`
3. Test locally: `python backend/scraper.py`
4. Check sites haven't changed their structure

### Documents not personalizing

1. Ensure templates exist: `ls -la data/*.docx`
2. Install python-docx: `pip install python-docx`
3. Check file paths in `cv_personalizer.py`

### Frontend not building

```bash
cd frontend
npm install
npm run build
npm run preview
```

---

## 📊 Data Structure

### job_offers.json

```json
{
  "offers": [
    {
      "id": "abc123def456",
      "company": "Intesa Sanpaolo",
      "title": "Corporate Finance Intern",
      "location": "Milano",
      "country": "Italy",
      "category": "banche_italiane",
      "description": "...",
      "link": "https://...",
      "posted_date": "2026-10-03T12:00:00Z",
      "deadline": "2026-10-31",
      "application_steps": "CV + Cover Letter + Assessment",
      "status": "new"
    }
  ],
  "total_count": 47,
  "last_updated": "2026-10-03T06:15:30Z"
}
```

### applications.json

```json
{
  "applications": [
    {
      "id": "app_123",
      "offerId": "abc123def456",
      "company": "Intesa Sanpaolo",
      "position": "Corporate Finance Intern",
      "status": "applied",
      "applied_date": "2026-10-03T14:30:00Z",
      "interview_date": null,
      "notes": "..."
    }
  ],
  "stats": {
    "total_applications": 5,
    "applied": 5,
    "in_review": 1,
    "rejected": 0,
    "offers": 0
  }
}
```

---

## 🚀 Deployment

### GitHub Pages Setup

1. Go to: Settings → Pages
2. Set source to "GitHub Actions"
3. Save
4. Workflow automatically deploys `frontend/dist` to GitHub Pages
5. Site available at: `https://[username].github.io/internship-tracker-2027`

### GitHub Actions Setup

1. Workflow automatically runs on schedule
2. Manual trigger: Actions tab → Daily Scraping → "Run workflow"
3. View logs for debugging
4. Scraper commits results automatically

### Environment Variables (Optional)

If you add authentication for protected sites, create a `.env` file:

```
COMPANY_USERNAME=your_email
COMPANY_PASSWORD=your_password
```

> ⚠️ Never commit `.env` files!

---

## 📈 Future Enhancements

- [ ] Email notifications for new opportunities
- [ ] Interview prep resources per company
- [ ] Salary/compensation data
- [ ] Candidate comparison tool
- [ ] Interview date scheduler
- [ ] Rejection feedback tracker
- [ ] Offer comparison matrix
- [ ] LinkedIn integration for connections
- [ ] Application timeline visualization
- [ ] Success rate analytics by company

---

## 💡 Pro Tips

1. **Keep templates updated** → Add new skills/experiences regularly
2. **Use meaningful notes** → Add context about why you're interested
3. **Track interview feedback** → Note common questions by company
4. **Export data** → Use JSON data for further analysis
5. **Review rejections** → Learn from feedback to improve future applications
6. **Network** → Combine tracker with LinkedIn outreach

---

## 📞 Support & Contact

**Built by:** Carlo Bisaglia  
**Email:** carlopt21@gmail.com  
**LinkedIn:** [Carlo Bisaglia](https://linkedin.com/in/carlo-bisaglia)  
**Location:** Lugano, Switzerland  
**Program:** Master in Finance (Digital Finance Track), USI

---

## 📄 License

MIT License - Use freely for your own job search!

```
Copyright (c) 2026 Carlo Bisaglia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software to deal in the software without restriction...
```

---

## 🙏 Acknowledgments

Built with:
- React, Vite, TailwindCSS (frontend)
- Python, BeautifulSoup, Requests (backend)
- GitHub Actions, GitHub Pages (automation & hosting)
- python-docx (document generation)

---

**Last Updated:** October 3, 2026  
**Status:** Production Ready ✅

🚀 *Happy job hunting! May this tracker help you land your dream internship!* 🎓
