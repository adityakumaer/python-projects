import os

file_name = "01_contacts.csv"

def add_contact():
    found = True
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write(f"Name, phone")
            found = False

    if found:
        with open(file_name, "a") as f:
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            f.write(f"\n{name}, {phone}")
            print("Contact added successfully.")


def view_contacts():
    with open(file_name, "r") as f:
        contacts = f.readlines()
        if len(contacts) <= 1:
            print("No contacts found.")
            return
        print("Contacts:")
        for contact in contacts[1:]:
            name, phone = contact.strip().split(", ")
            print(f"Name: {name} | Phone: {phone}")


def search_contact():
    name_to_search = input("Enter the name of the contact to search: ")
    with open(file_name, "r") as f:
        contacts = f.readlines()
        for contact in contacts[1:]:
            name, phone = contact.strip().split(", ")
            if name.lower() == name_to_search.lower():
                print(f"Name: {name} | Phone: {phone}")
                return
        print("Contact not found.")


def update_contact():
    name_to_update = input("Enter the name of the contact to update: ")
    with open(file_name, "r") as f:
        contacts = f.readlines()
    
    updated_contacts = []
    found = False
    for contact in contacts:
        name, phone = contact.strip().split(", ")
        if name.lower() == name_to_update.lower():
            new_phone = input("Enter the new phone number: ")
            updated_contacts.append(f"{name}, {new_phone}\n")
            found = True
        else:
            updated_contacts.append(contact)
    
    if found:
        with open(file_name, "w") as f:
            f.writelines(updated_contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")


def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    with open(file_name, "r") as f:
        contacts = f.readlines()
    
    updated_contacts = []
    found = False
    for contact in contacts:
        name, phone = contact.strip().split(", ")
        if name.lower() == name_to_delete.lower():
            found = True
            continue
        updated_contacts.append(contact)
    
    if found:
        with open(file_name, "w") as f:
            f.writelines(updated_contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

main()