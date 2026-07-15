import os
import requests
import csv
from datetime import datetime


filename = "weather_data.csv"
api_key = "ENTER_YOUR_API_KEY_HERE"

if not os.path.exists(filename):
    with open(filename,"w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "city", "temperature", "condition"])


def get_weather_data():
    city = input("Enter the city name: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(filename,"r", newline="") as file:
        writer = csv.DictReader(file)
        for row in writer:
            if row["city"].lower() == city.lower() and row["date"] == date:
                print(f"Weather data for {city} on {date} already exists in the CSV file.")
                print(f"{row['date']} : {row['city']} : {row['temperature']} : {row['condition']}")
                return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            print("API Error")
            return
        
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["main"]

        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, city.title(), temperature, condition])
            print(f"Logged: {temperature}°C, {condition} for {city.title()} on {date}")

    except Exception as e:
        print("failed to fetch weather data:")    


def view_weather_data():
    with open(filename, "r", newline="") as file:
        reader = list(csv.reader(file))
        if len(reader) <= 1:
            print("No weather data logged yet.")
            return
        print("\nWeather Data:")
        for row in reader[1:]:
            print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")


def main():
    while True:
        print("\nWeather Data Logger")
        print("1. Get weather data for a city")
        print("2. View logged weather data")
        print("3. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                get_weather_data()
            case "2":
                view_weather_data()
            case "3":
                print("Exiting the program.")
                exit()
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  