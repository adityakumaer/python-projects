import os
import requests
import textwrap
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont


url = "https://quotes.toscrape.com/"
output_file = "quotes"

def fetch_quotes(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quotes: {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    quote_data = []
    for quote in quotes:
        text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        quote_data.append((text, author))
    return quote_data


def create_image(text, author, index):
    width, height = 400, 300
    background_color = "#f8d77f"
    text_color = "#262626"

    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()
    author_font = ImageFont.load_default()

    wrapped = textwrap.fill(text, width=60)
    author_text = f"- {author}"

    y_text = 80
    draw.text((40, y_text), wrapped, font=font, fill=text_color)

    y_text += wrapped.count("\n") * 15 + 40
    draw.text((240, y_text), author_text, font=author_font, fill=text_color)

    if not os.path.exists(output_file):
        os.makedirs(output_file)

    filename = os.path.join(output_file, f"quote_{index + 1}.png")
    image.save(filename)
    print(f"Saved: {filename}")


def main():
    quotes = fetch_quotes(url)
    for index, (text, author) in enumerate(quotes):
        create_image(text, author, index)

if __name__ == "__main__":
    main()