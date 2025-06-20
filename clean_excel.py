import pandas as pd
from datetime import date

def clean(all_books):
    df = pd.DataFrame(all_books)

    # remove duplicates
    df = df.drop_duplicates()

    # Preview cleaned data
    print(df.head())

    # Save to Excel or CSV
    df.to_csv("data/cleaned_books.csv", index=False)
    df.to_excel("data/cleaned_books.xlsx", index=False)