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

add_contact()