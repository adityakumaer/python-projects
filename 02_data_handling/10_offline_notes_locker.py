import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

vault_file = "vault.json"
key_file = "secret.key"


def create_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)

    else:
        with open(key_file, "rb") as f:
            key = f.read()

    return key

fernet = Fernet(create_key())

def load_vault():
    if not os.path.exists(vault_file):
        return []
    else:
        with open(vault_file, "r") as f:
            return json.load(f)
        
def save_vault(data):
    with open(vault_file, "w") as f:
        json.dump(data, f, indent=4)

def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    encrypted_title = fernet.encrypt(title.encode()).decode()
    encrypted_content = fernet.encrypt(content.encode()).decode()

    vault = load_vault()
    vault.append({
        "title": encrypted_title,
          "content": encrypted_content,
            "timestamp": timestamp
        })
    
    save_vault(vault)
    print("✅ Note added successfully.")

def list_notes():
    vault = load_vault()
    if not vault:
        print("No notes found.")
        return

    print("Your Notes:")
    for i, note in enumerate(vault, 1):
        decrypted_title = fernet.decrypt(note['title'].encode()).decode()
        print(f"{i}. {decrypted_title} (Created on: {note['timestamp']})")

def view_note():
    vault = load_vault()
    if not vault:
        print("No notes found.")
        return
    print("")
    list_notes()
    choice = int(input("Enter the note number to view: ")) - 1

    if 0 <= choice < len(vault):
        note = vault[choice]
        decrypted_title = fernet.decrypt(note['title'].encode()).decode()
        decrypted_content = fernet.decrypt(note['content'].encode()).decode()
        print(f"{decrypted_title} (Created on: {note['timestamp']}) \n\n{decrypted_content}")
    else:
        print("Invalid choice.")

def search_notes():
    vault = load_vault()
    if not vault:
        print("No notes found.")
        return

    keyword = input("Enter keyword to search: ").lower()

    
    found = [note for note in vault if keyword in fernet.decrypt(note['title'].encode()).decode().lower()]

    for notes in found:
        decrypted_title = fernet.decrypt(notes['title'].encode()).decode()
        print(f"Found: {decrypted_title} (Created on: {notes['timestamp']})")

def main():
    while True:
        print("\nOffline Notes Locker")
        print("1. Add Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Exit")

        choice = input("Choose an option: ")

        match choice:
            case "1": add_note()
            case "2": list_notes()
            case "3": view_note()
            case "4": search_notes()
            case "5": 
                print("Exiting...")
                break
            case _: print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()