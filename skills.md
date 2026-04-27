# Skills and Setup Guide for Indeo Gwon Real Estate Project

## Project Overview
This project is a web-based real estate listing viewer for Indeo Gwon area, built with HTML, CSS, JavaScript, and Chart.js. It includes data parsing from text files and interactive filtering of property listings.

## Technologies Used
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Charts**: Chart.js for data visualization
- **Data Processing**: Python for parsing raw listing data
- **Deployment**: Vercel (connected to GitHub for auto-deployment)

## Development Workflow
1. **Local Development**:
   - Run `python -m http.server 8000` to start local server
   - Open `http://localhost:8000/index.html` in browser

2. **Data Processing**:
   - Raw listings in `매물목록.txt`
   - Run `python parse_listings2.py` to generate `listings.json`
   - JSON data is loaded dynamically in the web app

3. **Version Control**:
   - All changes must be committed to Git
   - Push to GitHub repository
   - Vercel automatically deploys on push to main branch

## Git and Deployment Setup
### GitHub Repository
- Repository: [Create on GitHub](https://github.com/new)
- Name: `indeogwon-real-estate` (or similar)
- Make it public or private as preferred

### Vercel Deployment
1. Go to [Vercel](https://vercel.com)
2. Import GitHub repository
3. Set build settings:
   - Framework Preset: None (static HTML)
   - Root Directory: `/`
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
4. Deploy

### Workflow Rules
- **Every change** in this folder must be:
  1. `git add .`
  2. `git commit -m "descriptive message"`
  3. `git push origin main`
- Vercel will auto-deploy on push
- Check deployment status at Vercel dashboard

## File Structure
```
indeogwon/
├── index.html          # Main web page
├── listings.json       # Parsed listing data
├── parse_listings.py   # Original parser
├── parse_listings2.py  # Enhanced parser
├── 매물목록.txt         # Raw listing data
├── README.md           # Project readme
└── skills.md           # This file
```

## Key Features
- Interactive property listing filters (complex, price, size, direction)
- Responsive design with CSS Grid/Flexbox
- Chart visualizations for analysis
- Monthly payment calculator
- Tabbed interface for different sections

## Maintenance
- Update `매물목록.txt` with new listings
- Re-run `parse_listings2.py` to update `listings.json`
- Commit and push changes
- Vercel handles deployment automatically

## Notes
- Data is in Korean (real estate listings)
- Uses local JSON loading (works with Vercel)
- No backend required (static site)