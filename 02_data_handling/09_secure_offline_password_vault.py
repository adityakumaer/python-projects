import base64
import os

vault_file = 'password_vault.txt'

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()


def password_strength_check(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-+" for c in password)
    
    score = sum([length >= 8, has_upper, has_digit, has_special])
    return ["poor", "weak", "moderate", "strong"][min(score, 3)]


def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    strength = password_strength_check(password)

    line = f"{website} || {username} || {password}"
    encoded_line = encode(line)

    with open(vault_file, 'a') as file:
        file.write(encoded_line + "\n")

    print(f"✅ Credential saved")


def view_credentials():
    if not os.path.exists(vault_file):
        print("File not found")
        return

    with open(vault_file, 'r') as file:
        lines = file.readlines()

    if not lines:
        print("No credentials stored yet.")
        return

    print("\nStored Credentials:")
    for line in lines:
        decoded_line = decode(line.strip())
        website, username, password = decoded_line.split(" || ")
        hidden_password = '*' * len(password)
        print(f"website: {website} | username: {username} | password: {password}")


def update_password():
    if not os.path.exists(vault_file):
        print("File not found")
        return
    
    user_website = input(f"Enter website to update password: ").strip()
    with open(vault_file, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        decoded = decode(line.strip())
        website, username, password = decoded.split(" || ")

        if website == user_website:
            new_password = input(f"Enter new password for {website}: ").strip()
            strength = password_strength_check(new_password)
            updated_line = f"{website} || {username} || {new_password}"
            encoded_line = encode(updated_line)
            updated_lines.append(encoded_line + "\n")
            print(f"✅ Password updated for {website}")

        else:
            updated_lines.append(line)

        with open(vault_file, 'w') as file:
            file.writelines(updated_lines)



def main():
    while True:
        print("\nPassword Vault Menu:")
        print("1. Add Credential")
        print("2. View Credentials")
        print("3. Update Password")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1": add_credential()
            case "2": view_credentials()
            case "3": update_password()
            case "4":
                print("Exiting...")
                break
            case _: print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()