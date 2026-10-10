import random

# Define valid choices for user and computer
choices = ["rock", "paper", "scissors"]

# Get user and computer choice
computer_choice = random.choice(choices)
user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()

# Validate user choice, then print the winner or whether it's a draw
if user_choice not in choices:
    print("You must choose either 'rock', 'paper', or 'scissors'.")
else:
    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("User wins!")
    else:
        print("Computer wins!")
