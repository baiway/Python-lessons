import random

# Define valid choices for user and computer
choices = ["rock", "paper", "scissors", "lizard", "spock"]

# Get user and computer choice
computer_choice = random.choice(choices)
user_choice = input("Enter 'rock', 'paper', 'scissors', 'lizard', or 'Spock': ").lower()

# Validate user choice, then print the winner or whether it's a draw
if user_choice not in choices:
    print("You must choose either 'rock', 'paper', 'scissors', 'lizard', or 'Spock'.")
else:
    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (
        (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "rock" and computer_choice == "lizard")
        or (user_choice == "lizard" and computer_choice == "spock")
        or (user_choice == "spock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "lizard")
        or (user_choice == "lizard" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "spock")
        or (user_choice == "spock" and computer_choice == "rock")
        or (user_choice == "rock" and computer_choice == "scissors")
    ):
        print("User wins!")
    else:
        print("Computer wins!")
