# 📚 Book Price Tracker & Report Bot

A fully automated Python bot that scrapes book prices from [BooksToScrape.com](https://books.toscrape.com), cleans the data, uploads it to Google Sheets, and sends a daily email report with an attached Excel file.

---

## 🔧 Features

✅ Scrapes title, price, availability for 1000 books  
✅ Handles pagination across 50+ pages  
✅ Cleans and formats scraped data using `pandas`  
✅ Saves to both Excel and CSV formats  
✅ Uploads the data to a connected Google Sheet  
✅ Sends an email with the daily report as an attachment  
✅ Fully automated with scheduled daily execution via `schedule`  
✅ Ready for deployment (e.g., Replit, Render)

---

## 🚀 Technologies Used

- `requests` + `BeautifulSoup` — for scraping
- `pandas` — for data cleaning & transformation
- `openpyxl` — for Excel export
- `gspread` + `google-auth` — for Google Sheets integration
- `smtplib` + `email.mime` — for sending email reports
- `schedule` — for daily task automation

---

## 📦 Project Structure
daily-books-excel-report/
│
├── credentials.json # Google Service Account Key
├── data/cleaned_books.xlsx # Output report file
├── scraping.py # Web Scraping script
├── clean_excel.py # Data Entry script
├── upload_to_google_sheet.py # Google Sheet script
├── report_emails.py # Email Reeport script
├── index.py # start script
├── .env # (Optional) for email and sheet secrets
└── README.md # This file

---

## ⚙️ How to Run

### 1. Clone this repo
```bash
git clone https://github.com/LukaC-Senior/daily-books-excel-report.git
cd daily-books-excel-report

python -m venv venv

pip install -r requirements.txt

python index.py

