import json
import os

FILE_NAME = "contacts.json"


# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add a new contact
def add_contact(contacts):
    print("\n=== ADD CONTACT ===")

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


# View all contacts
def view_contacts(contacts):
    print("\n=== CONTACT LIST ===")

    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\n{i}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print(f"   Address: {contact['address']}")


# Search for a contact
def search_contact(contacts):
    print("\n=== SEARCH CONTACT ===")

    search = input("Enter name or phone number to search: ").lower()

    found = False

    for contact in contacts:
        if (search in contact["name"].lower()
                or search in contact["phone"]):

            print("\nContact found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])

            found = True

    if not found:
        print("Contact not found.")


# Update a contact
def update_contact(contacts):
    print("\n=== UPDATE CONTACT ===")

    if not contacts:
        print("No contacts available.")
        return

    view_contacts(contacts)

    try:
        number = int(input("\nEnter contact number to update: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return

        contact = contacts[number - 1]

        print("\nEnter new details:")

        name = input(f"Enter name ({contact['name']}): ")
        phone = input(f"Enter phone ({contact['phone']}): ")
        email = input(f"Enter email ({contact['email']}): ")
        address = input(f"Enter address ({contact['address']}): ")

        if name:
            contact["name"] = name

        if phone:
            contact["phone"] = phone

        if email:
            contact["email"] = email

        if address:
            contact["address"] = address

        save_contacts(contacts)

        print("Contact updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Delete a contact
def delete_contact(contacts):
    print("\n=== DELETE CONTACT ===")

    if not contacts:
        print("No contacts available.")
        return

    view_contacts(contacts)

    try:
        number = int(input("\nEnter contact number to delete: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return

        deleted_contact = contacts.pop(number - 1)

        save_contacts(contacts)

        print(f"Contact '{deleted_contact['name']}' deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Main program
contacts = load_contacts()

while True:

    print("\n=== CONTACT BOOK ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        update_contact(contacts)

    elif choice == "5":
        delete_contact(contacts)

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")