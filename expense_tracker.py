import datetime
expenses = []

def add_expense():
    amount = float(input('Enter amount: '))
    category = input('Select category Food, Travel, Shopping etc: ')
    note = input('Enter note: (optional): ')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    expense = {
        'amount': amount,
        'category': category,
        'note': note,
        'date': date
    }

    expenses.append(expense)
    print('expense added successfully!\n')

def view_expenses():
    if not expenses:
        print('No expenses recorded yet.\n')
        return
    print('\n All Expenses ')
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['note']}")
    print()

# Function to delete expense
def delete_expense():
    if not expenses:
        print("No expenses to delete.\n")
        return
    
    view_expenses()
    try:
        index = int(input("Enter the expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            print(f"Deleted: {deleted['category']} | ₹{deleted['amount']} | {deleted['note']}\n")
        else:
            print("Invalid expense number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


while True:
    user_input = input('Enter 1 for add expense, enter 2 for view expense, enter 3 for delete expense , enter 4 to exit: ')

    if user_input == '1':
        add_expense()
    elif user_input == '2':
        view_expenses()
    elif user_input == '3':
        delete_expense()
    elif user_input == '4':
        print('exit, Bye')
        break
    else:
        print('Invalid Input, please try again!')