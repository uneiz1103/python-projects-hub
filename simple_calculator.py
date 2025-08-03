def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if(num2 == num1):
        return "Cannot divide by zero"
    return num1 / num2

while True:
    print("\nSelect Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    fst_no = float(input("Enter 1st number: "))
    snd_no = float(input("Enter 2nd number: "))

    if choice == '1':
        print(f"Result: {add(fst_no, snd_no)}")
    elif choice == '2':
        print(f"Result: {sub(fst_no, snd_no)}")
    elif choice == '3':
        print(f"Result: {mul(fst_no, snd_no)}")
    elif choice == '4':
        print(f"Result: {div(fst_no, snd_no)}")
    else:
        print("Invalid input")

    again = input("\nDo you want to calculate again? (yes/no): ")
    if again.lower() != 'yes':
        print("Goodbye!")
        break
