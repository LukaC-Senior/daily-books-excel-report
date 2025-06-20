import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

def upload_data():
    # Load your cleaned data
    df = pd.read_excel("data/cleaned_books.xlsx")  # or use .csv if you saved that

    # Load credentials
    creds = Credentials.from_service_account_file("credentials.json")
    client = gspread.authorize(creds)

    # Open your Google Sheet by name
    spreadsheet = client.open("Daily_Book_Prices")  # Change this to your actual sheet name
    sheet = spreadsheet.sheet1  # First sheet (or use .worksheet('SheetName'))

    # Clear old data
    sheet.clear()

    # Upload new data (convert DataFrame to list of lists)
    sheet.update(
        [df.columns.values.tolist()] + df.values.tolist()
    )