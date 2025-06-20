import schedule
import time
from datetime import datetime
from scraping import scrap_all_books
from upload_to_google_sheet import upload_data
from report_emails import do_report

def job():
    print(f"Job started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Scrape data
    scrap_all_books()

    # Upload to Google Sheets
    upload_data()

    # Send email with attachment
    do_report()

# Schedule the job every day at 08:00
schedule.every().day.at("08:00").do(job)

print("Automation started. Waiting for scheduled time...")

while True:
    schedule.run_pending()
    time.sleep(60)