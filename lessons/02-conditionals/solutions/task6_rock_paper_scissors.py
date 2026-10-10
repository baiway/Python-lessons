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

    if user_choice == "rock":
        if computer_choice == "scissors":
            print("User wins!")
        elif computer_choice == "paper":
            print("Computer wins!")
        else:
            print("It's a draw!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("User wins!")
        elif computer_choice == "scissors":
            print("Computer wins!")
        else:
            print("It's a draw!")
    else:  # user_choice must be "scissors"
        if computer_choice == "paper":
            print("User wins!")
        elif computer_choice == "rock":
            print("Computer wins!")
        else:
            print("It's a draw!")
