import random

options = ['rock', 'paper', 'scissors']


while True:
    user_choice = input("\nChoose rock, paper or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(options)
    print(f'Computer choice: {computer_choice}')

    if user_choice == computer_choice:
        print("It's a Tie")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("You Win!!")
    else:
        print("You loose!!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 🎉")
        break
