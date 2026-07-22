import requests
import time
import sqlite3
from datetime import datetime

api_url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": "false"
}

db_file = "crypto_data.db"


def fetch_crypto_data():
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


def create_table():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            coin TEXT,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()


def save_to_db(crypto_data):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    for coin in crypto_data:
        cursor.execute('''
            INSERT INTO crypto_prices (timestamp, coin, price)
            VALUES (?, ?, ?)
        ''', (timestamp, coin['id'], coin['current_price']))

    conn.commit()
    conn.close()
    print("\nPrice saved to database")


def search_coin(coin_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT timestamp, price FROM crypto_prices WHERE coin = ?
                   ORDER BY timestamp DESC
                   LIMIT 1
    ''', (coin_name,))
    results = cursor.fetchall()
    conn.close()
    if results:
        print(f"\nDate: {results[0][0]}, Price: {results[0][1]}")
    else:
        print("Coin not found.")

def main():
    create_table()

    while True:
        print("\n1. Fetch and save crypto data")
        print("2. Search for a latest price of a coin")
        print("3. Exit")

        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            crypto_data = fetch_crypto_data()
            save_to_db(crypto_data)

        elif choice == "2":
            coin_name = input("Enter the coin name (e.g., bitcoin, ethereum): ")
            search_coin(coin_name)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()