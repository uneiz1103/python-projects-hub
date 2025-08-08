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
        print("📭 No contacts found.\n")
    else:
        print("\n📒 Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-" * 20)

add_contact()
view_contacts()