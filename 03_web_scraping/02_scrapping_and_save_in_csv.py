import csv
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
file_name = "scraped_data.csv"

def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch page: \n{e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    posts = soup.select("span.titleline > a")

    data = []
    for post in posts:
            title = post.text.strip()
            link = post.get("href")
            data.append({"title": title, "link": link})
    return data


def save_to_csv(data):
    if not data:
        print("No data to save.")
        return
     
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link"])
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Data saved to {file_name}")


def main():
    data = fetch_data(url)
    print(f"✅ Scraped {len(data)} posts")
    save_to_csv(data)


if __name__ == "__main__":
    main()