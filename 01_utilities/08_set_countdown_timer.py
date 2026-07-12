import time

class smaller_number(Exception):
     pass



while True:
    try:
        user = int(input("Ener the time in second: "))
        if user < 1:
            raise smaller_number("Enter a number greater than 0")
        break
    except ValueError:
        raise ValueError("Enter a valid number")
    
print("Timer started...")
for clock in range(user, 0, -1):
        minutes, seconds = divmod(clock , 60)
        remaining = f"{minutes:02}:{seconds:02}"
        print(f"Time left: {remaining}", end="\r")
        time.sleep(1)
print("\nTime's up!")