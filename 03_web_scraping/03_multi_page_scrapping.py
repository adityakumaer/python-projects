import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin


url = "https://books.toscrape.com/"
start = "catalogue/page-1.html"
output = "scraped.json"
count = 100



def scrap_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch page: \n{e}")
        return [], None
    
    soup = BeautifulSoup(response.text, "html.parser")
    book = []

    for artical in soup.select("article.product_pod"):
        title = artical.select_one("h3 > a").get("title")
        price = artical.select_one("p.price_color").text.strip()
        book.append({"title": title, "price": price})

    next_page = soup.select_one("li.next > a")
    next_page_url = urljoin(url, next_page.get("href")) if next_page else None

    return book, next_page_url


def main():

    all_books = []
    current_page = start

    while current_page and len(all_books) < count:
        page_url = urljoin(url, current_page)
        print(f"Scraping page: {page_url}")
        books, next_page_url = scrap_page(page_url)
        all_books.extend(books)
        current_page = next_page_url

    all_books = all_books[:count]

    with open(output, "w") as f:
        json.dump(all_books, f, indent=4)

    print(f"✅ Scraped {len(all_books)} books and saved to {output}")


if __name__ == "__main__":
    main()