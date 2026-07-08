import random

from pyparsing import line


def create_account():
    name = input("\nEnter your name: ")
    age = input("Enter your age: ")

    account_number = random.randint(1000000000, 9999999999)
    account_number = list(str(account_number))
    random.shuffle(account_number)
    account_number = ''.join(account_number)

    password = input("Enter your password: ")
    amount = 0

    with open("accounts.csv", "a") as file:
        file.write(f"{name},{age},{account_number},{password},{amount}\n")

    print("Account created successfully!")
    print(f"\nYour account number is: {account_number}")


def add_amount(account_number, amount):
    with open("accounts.csv", "r") as file:
        lines = file.readlines()

    with open("accounts.csv", "w") as file:
        for line in lines:
            name, age, acc_num, passw, bal = line.strip().split(",")
            if acc_num == account_number:
                bal = str(float(bal) + float(amount))
            file.write(f"{name},{age},{acc_num},{passw},{bal}\n")

    print(f"\nAmount added successfully! New balance: {bal}")


def withdraw_amount(account_number, amount):
    with open("accounts.csv", "r") as file:
        lines = file.readlines()

    with open("accounts.csv", "w") as file:
        for line in lines:
            name, age, acc_num, passw, bal = line.strip().split(",")
            if acc_num == account_number:
                if float(bal) >= float(amount):
                    bal = str(float(bal) - float(amount))
                    print(f"\nAmount withdrawn successfully! New balance: {bal}")
                else:
                    print("\nInsufficient balance.")
            file.write(f"{name},{age},{acc_num},{passw},{bal}\n")


def login():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

    with open("accounts.csv", "r") as file:
        for line in file:
            name, age, acc_num, passw, bal = line.strip().split(",")
            if acc_num == account_number and passw == password:
                print(f"\nWelcome back, {name}!")
                
                while True:
                    print("\n1. Check Balance")
                    print("2. Add amount")
                    print("3. Withdraw amount")
                    print("4. Change password")
                    print("5. Log-out")

                    user = input("Enter your choice (1, 2, 3, 4, or 5): ")

                    if user == "1":
                        with open("accounts.csv", "r") as file:
                            for line in file:
                                name, age, acc_num, passw, bal = line.strip().split(",")
                                if acc_num == account_number:
                                    print(f"\nYour current balance is: {bal}")
                                    break

                    elif user == "2":
                        add = input("\nEnter the amount to add: ")
                        add_amount(account_number, add)

                    elif user == "3":
                        withdraw = input("\nEnter the amount to withdraw: ")
                        withdraw_amount(account_number, withdraw)

                    elif user == "4":
                        old_password = input("\nEnter your old password: ")
                        if old_password != password:
                            print("\nIncorrect old password. Please try again.")
                            continue
                        new_password = input("\nEnter your new password: ")
                        confirm_password = input("Confirm your new password: ")
                        if new_password != confirm_password:
                            print("\nPasswords do not match. Please try again.")
                            continue
                        
                        with open("accounts.csv", "r") as file:
                            lines = file.readlines()

                        with open("accounts.csv", "w") as file:
                            for line in lines:
                                name, age, acc_num, passw, bal = line.strip().split(",")
                                if acc_num == account_number:
                                    passw = new_password
                                file.write(f"{name},{age},{acc_num},{passw},{bal}\n")

                        print("\nPassword changed successfully.")

                    elif user == "5":
                        print("\nLogged out successfully.")
                        main()

                    else:
                        print("\nInvalid choice. Please try again.")

    print("\nInvalid account number or password.")


def know_your_account_number():
    name = input("\nEnter your name: ")
    age = input("Enter your age: ")
    password = input("Enter your password: ")

    with open("accounts.csv", "r") as file:
        found = False
        for line in file:
            acc_name, acc_age, acc_num, passw, bal = line.strip().split(",")
            if acc_name == name and acc_age == age and passw == password:
                print(f"\nYour account number is: {acc_num}")
                found = True
                break
        if not found:
            print("\nNo account found with the provided details.")


def forget_password():
    account_number = input("\nEnter your account number: ")
    new_password = input("\nEnter your new password: ")
    confirm_password = input("Confirm your new password: ")

    if new_password != confirm_password:
        print("\nPasswords do not match. Please try again.")
        return
    
    with open("accounts.csv", "r") as file:
        lines = file.readlines()

    with open("accounts.csv", "w") as file:
        for line in lines:
            name, age, acc_num, passw, bal = line.strip().split(",")
            if acc_num == account_number:
                passw = new_password
            file.write(f"{name},{age},{acc_num},{passw},{bal}\n")

    print("\nPassword changed successfully.")


def main():
    print("\nWelcome to ABC Bank")
    while True:
        print("\n1. Create Bank Account")
        print("2. Log-in Bank Account")
        print("3. Know Your Account Number")
        print("4. Exit")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == "1":
            create_account()
        
        elif choice == "2":
            print("\n1. login")
            print("2. forgot password")

            choice = input("Enter your choice (1 or 2): ")
            
            if choice == "1":
                login()
            elif choice == "2":
                forget_password()

        elif choice == "3":
            know_your_account_number()

        elif choice == "4":
            print("\nThank you for using ABC Bank. Goodbye!")
            exit()
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()