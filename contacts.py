contacts = []

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contact(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for i, contacts in enumerate(contacts, start=1):
            print(f"{i}. Name: {contacts["name"]}, Phone: {contacts["phone"]}, Email: {contacts["email"]}")

def search_contact(contacts):
    search_contact = input("Enter contact name to search: ")
    for contact in contacts:
        if contact["name"].lower() == search_contact.lower():
            print(f"contact found: Name: {contact["name"]}, Phone: {contact["phone"]}, Email: {contact["email"]}")
            return
    print("Contact not found.")

def delete_contact(contacts):
    delete_contact = input("Enter contact name to delete: ")
    for contact in contacts:
        if contact["name"].lower() == delete_contact.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    contacts = [] 
    while True:
        print("Contact Book") 
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
