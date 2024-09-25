import random

# Define valid choices for user and computer
choices = ["rock", "paper", "scissors"]

# Get user and computer choice
computer_choice = random.choice(choices)
user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()

# Validate user choice
if user_choice not in choices:
    raise ValueError("You must choose either 'rock', 'paper', or 'scissors'.")

# Print computer choice
print("The computer chose: ", computer_choice)

# Print the winner or whether it's a draw
if user_choice == "rock":
    if computer_choice == "scissors":
        print("User wins!")
    elif computer_choice == "paper":
        print("Comptuer wins!")
    else:
        print("It's a draw!")
if user_choice == "paper":
    if computer_choice == "rock":
        print("User wins!")
    elif computer_choice == "scissors":
        print("Comptuer wins!")
    else:
        print("It's a draw!")
if user_choice == "scissors":
    if computer_choice == "paper":
        print("User wins!")
    elif computer_choice == "rock":
        print("Comptuer wins!")
    else:
        print("It's a draw!")