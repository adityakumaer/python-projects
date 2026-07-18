import requests
from bs4 import BeautifulSoup


url = "https://freshjuice.dev/tools/heading-extractor/"

def get_headings(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch page: \n{e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")

    tags = soup.find_all("h3")
    headings = []
    for tag in tags:
        heading = tag.get_text(strip=True)
        if heading and heading.lower() != "contents":
            headings.append(heading)

            
    for i in headings:
        print(i)

if __name__ == "__main__":
    get_headings(url)