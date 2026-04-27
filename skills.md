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

## Efficiency Tips — 소스 최적화 & 토큰 절약

### 현재 구조의 비효율 포인트
- `index.html` 한 파일에 스타일/데이터/JS가 모두 있어 1,500줄↑. Claude가 수정 시 전체 파일을 읽어야 함.
- `complexes` 배열(~140줄), `recommendedData` 배열, 블라인드 데이터가 인라인으로 존재.

### 개선 방법 (토큰 절약 효과 높은 순)

#### 1. 데이터 분리 → JSON 파일화 (효과 ★★★)
```
complexes_data.json   # 단지 정보 배열
recommended_data.json # 추천매물 Top3
blind_data.json       # 블라인드 의견 요약
```
- `complexes`, `top3ByComplex`, 블라인드 스레드 데이터를 JSON으로 분리
- `fetch()`로 로드. index.html은 렌더 로직만 남김 (~300줄 절감)
- Claude 수정 시 해당 JSON 파일만 읽으면 됨

#### 2. CSS 분리 → style.css (효과 ★★)
- 현재 CSS가 ~230줄 인라인. `style.css`로 분리하면 index.html 가독성 향상
- 스타일 변경 시 CSS 파일만 편집

#### 3. 차트 설정 분리 (효과 ★)
- Chart.js 설정 3개를 `charts.js`로 분리
- 데이터 변경과 독립적으로 관리 가능

### 수정 시 효율적인 접근법
- 단지 정보 수정: `complexes_data.json`만 읽고 수정
- 교통/학군 텍스트 수정: `grep`으로 키워드 찾아 Edit 도구로 직접 수정
- 새 탭 추가: HTML section 추가 + nav button 추가 2군데만 편집
- 추천매물 업데이트: `recommended_data.json`만 수정

### Vercel 배포 주의사항
- JSON 분리 후 `fetch('*.json')`은 Vercel에서 정상 동작 (정적 파일 서빙)
- `listings.json`과 동일한 방식으로 로드 가능