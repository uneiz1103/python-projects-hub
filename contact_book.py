contacts = {}

def add_contact():
    name = input('Enter name: ').lower()
    phone = input('Enter phone: ')
    email = input('Enter email: ')

    contacts[name] = {
        'phone' : phone,
        'email' : email
    }
    print(f'Contact for {name} added sucessfully')

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-" * 20)

def search_contact():
    name = input("Enter name to search: ").lower()
    if name in contacts:
        print(f"\nContact found for {name}:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}\n")
    else:
        print(f"Contact for '{name}' not found.\n")

def delete_contact():
    name = input("Enter name to delete: ").lower()
    if name in contacts:
        del contacts[name]
        print(f"Contact for '{name}' deleted.\n")
    else:
        print(f"Contact for '{name}' not found.\n")


add_contact()
view_contacts()
search_contact()