
def calculate_minutes_alive(age):
    try:
        age = int(age)
        if age <= 0:
            raise ValueError("Age cannot be zero or negative.")

        days_in_year = 365.25
        hours_in_day = 24
        minutes_in_hour = 60
        Days_alive = age * days_in_year 
        Hours_alive = Days_alive * hours_in_day
        minutes_alive = Hours_alive * minutes_in_hour

        return round(Days_alive, 2), round(minutes_alive, 2), round(Hours_alive, 2)
    
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid age.")
    


print("\nWelcome to the Minutes Alive Calculator!")
while True:
    print("1. Calculate Minutes Alive")
    print("2. Exit")
    choice = input("Please select an option (1 or 2): ").strip()

    
    if choice == "1":
        age = input("Please enter your age: ").strip()
        days_alive, minutes_alive, hours_alive = calculate_minutes_alive(age)

        print(f"\nYou have been alive for approximately\n{days_alive} days\n{hours_alive} hours\n{minutes_alive} minutes.")

        user_choice = input("\nWould you like to calculate again? (yes/no): ").strip().lower()
        if user_choice != "yes":
            print("Exiting the program. Thanks for using!")
            break

    if choice == "2":
        print("Exiting the program. Thanks for using!")
        break
