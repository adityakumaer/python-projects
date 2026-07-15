import csv
import matplotlib.pyplot as plt

filename = "weather_data.csv"

def visualize_weather_data():

    dates = []
    temperatures = []
    conditions = {}

    with open(filename, "r", newline="") as file:
        reader = list(csv.reader(file))
        if len(reader) <= 1:
            print("No weather data logged yet.")
            return
        print("\nWeather Data:")
        for row in reader[1:]:
            dates.append(row[0])
            temperatures.append(float(row[2]))
            conditions[row[3]] = conditions.get(row[3], 0) + 1

    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker='o', linestyle='-', color='b')
    plt.title("Weather Data Visualization")
    plt.xlabel("Dates")
    plt.ylabel("Temperature (°C)")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(conditions.keys(), conditions.values(), color='orange')
    plt.title("Weather Conditions")
    plt.xlabel("Conditions")
    plt.ylabel("Days")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

visualize_weather_data()