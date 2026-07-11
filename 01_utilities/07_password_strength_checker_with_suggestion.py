import string
import getpass
import random


def password_strength_checker(password):
    error = []

    if password <= "8":
        error.append("Less than 8 characters")
    if not any(check.islower() for check in password):
        error.append("Missing lower case letter")
    if not any(check.isupper() for check in password):
        error.append("Missing upper case letter")
    if not any(check.isdigit() for check in password):
        error.append("Missing a digit")
    if not any(check in string.punctuation for check in password):
        error.append("Missing special character")
    return error


def password_suggestion(size=8):
    starting = string.ascii_letters
    mid = string.punctuation
    ending = string.digits

    starting = "".join(random.choice(starting) for _ in range(int((size / 3 ))))
    mid = "".join(random.choice(mid) for _ in range(int(size / 3)))
    ending = "".join(random.choice(ending) for _ in range(int((size / 3))))
    all_ = starting + mid + ending
    
    if all_ != size:
        last = "".join(random.choice(ending) for _ in range(1))
        all_ += last

    return all_


while True:
    print("\nWelcome to Password checker and suggestion")
    print("1. Check your password")
    print("2. Get suggestion")
    print("3. Exit")

    user = int(input("Select a number: "))
    match user:
        case 1:
            pass_ = getpass.getpass("Enter a password: ")
            error = password_strength_checker(pass_)
            if error:
                print("\nyou got weak password!")
                for weak in error:
                    print(f"- {weak}")
            else:
                print("\nGood Password!")
        case 2:
            size = input("Enter the size of your password (optional): ")
            size = int(size)
            if size:
                suggestion = password_suggestion(size)
                print("\nsuggestion for you:")
                print(suggestion)
            else:
                suggestion = password_suggestion()
                print("\nsuggestion for you:")
                print(suggestion)
        case 3:
            print("Exiting...")
            break

        case _:
            print("Enter a valid number")
            break
