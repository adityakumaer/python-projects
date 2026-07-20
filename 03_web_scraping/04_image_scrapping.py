import os
import re
import requests
import wget
from urllib.parse import urljoin
from bs4 import BeautifulSoup


base_url = "https://books.toscrape.com/"
image_dir = "images"

def sanitize_filename(filename):
    return re.sub(r'[^\w\-_. ]', '', filename).replace(' ', '_')


def download_image(image_url, file_path):
    try:
        response = requests.get(image_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

    except requests.exceptions.RequestException as e:
        print(f"Failed to download image: \n{e}")
        return
    

def scrap_images(count=10):
    
    url = base_url
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:count]

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    for artical in books:
        title = artical.select_one("h3 > a").get("title")
        image_url = artical.find("img")["src"]
        image_url = urljoin(base_url, image_url)
        print(f"url: {image_url}")

        sanitized_title = sanitize_filename(title) + ".jpg"
        file_path = os.path.join(image_dir, sanitized_title)
        print(f"File_path -> {file_path}")

        print(f"Downloading: {title}")

        # download_image(image_url, file_path)   ### Download image using requests

        wget.download(image_url, file_path)   ### Download image using wget

    print("✅ All images downloaded successfully.")

if __name__ == "__main__":
    user = int(input("How many images you want to download? (default is 20): "))
    scrap_images(user)
