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

def update_expense():
    if not expenses:
        print("No expenses to update.\n")
        return
    
    view_expenses()
    try:
        index = int(input("Enter the expense number to update: ")) - 1
        if 0 <= index < len(expenses):
            print("Old Expense:", expenses[index])
            
            amount = float(input("Enter new amount: "))
            category = input("Enter new category: ")
            note = input("Enter new note: ")
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            expenses[index] = {
                'amount': amount,
                'category': category,
                'note': note,
                'date': date
            }
            print("Expense updated successfully!\n")
        else:
            print("Invalid expense number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def total_expense(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n Total Expense = ₹{total}\n")

while True:
    print("Enter 1 to Add Expense")
    print("Enter 2 to View Expenses")
    print("Enter 3 to Delete Expense")
    print("Enter 4 to Update Expense")
    print("Enter 5 to View Total Expense")
    print("Enter 6 to Exit")

    user_input = input('Enter Your Choice: ')

    if user_input == '1':
        add_expense()
    elif user_input == '2':
        view_expenses()
    elif user_input == '3':
        delete_expense()
    elif user_input == '4':
        update_expense()
    elif user_input == "5":
        total_expense(expenses)
    elif user_input == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.\n")