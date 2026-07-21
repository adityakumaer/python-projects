import os
import csv
import requests
import time
import schedule
from datetime import datetime

api_url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": "false"
}

csv_file = "crypto_prices.csv"


def fetch_crypto_data():
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


def save_to_csv(data):
    file_exists = os.path.exists(csv_file)
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "coin", "price"])
        
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        for coin in data:
            writer.writerow([timestamp, coin['id'], coin['current_price']])

    print("✅ Data saved to csv")


def job():
    print("Fetching crypto data...")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)

schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)