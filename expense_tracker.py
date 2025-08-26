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

add_expense()