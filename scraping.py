import requests
from bs4 import BeautifulSoup
from clean_excel import clean

base_url = "https://books.toscrape.com/"
    
def scrap_all_books():
    all_books = []
    next_page = "catalogue/page-1.html"

    while next_page:
    # Build full URL
        url = base_url + next_page
        print(f"Scraping: {url}")
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("article", class_="product_pod")

        for p in products:
            title = p.h3.a["title"]
            price = p.find("p", class_="price_color").text.strip()
            availability = p.find("p", class_="instock availability").text.strip()
            all_books.append((title, price, availability))

        # Find next page
        next_btn = soup.find("li", class_="next")
        if next_btn:
            next_page = "catalogue/" + next_btn.a["href"]
        else:
            next_page = None
    
    clean(all_books=all_books)

if __name__ == "__main__":
    scrap_all_books()
    
    



