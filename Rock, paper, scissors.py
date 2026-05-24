import random

choices = ["rock", "paper", "scissors"]
print("Welcome to Rock, Paper, Scissors!")
player_choice = input("Please enter your choice (rock, paper, scissors): ").lower()

if player_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(choices)
    computer_choice = random.choice(choices)
    print(f"You chose {player_choice}. Computer chose {computer_choice}.")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")