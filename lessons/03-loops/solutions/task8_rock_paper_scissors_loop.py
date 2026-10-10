import random

# Define valid choices for user and computer
choices = ["rock", "paper", "scissors"]

# Keep track of the score
user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter 'rock', 'paper', 'scissors' or 'quit': ").lower()

    # Exit the loop if the user wants to stop, or skip to the next round if
    # their choice isn't valid
    if user_choice == "quit":
        break
    if user_choice not in choices:
        print("You must choose either 'rock', 'paper', or 'scissors'.")
        continue

    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")

    # Print the winner of this round and update the score
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("User wins!")
        user_score = user_score + 1
    else:
        print("Computer wins!")
        computer_score = computer_score + 1

print(f"Final score: User {user_score} - {computer_score} Computer")
