import random 

secret_number = random.randint(1,100)

print('Welcome to the number Guessing Game!')
print('Enter number between 1 to 100')

attempts = 0

while True:
    guess = input('Enter your guess: ')

    guess = int(guess)

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congrulations you win")
        break

print(f"Number of attempts:  {attempts}")