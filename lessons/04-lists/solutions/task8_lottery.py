import random

# Pick 6 different random numbers
winning_numbers = []
while len(winning_numbers) < 6:
    number = random.randint(1, 59)
    if number not in winning_numbers:
        winning_numbers.append(number)
winning_numbers.sort()

# Get the user's numbers
print("Enter your 6 numbers (between 1 and 59).")
user_numbers = []
for i in range(6):
    user_numbers.append(int(input(f"Number {i + 1}: ")))

# Count how many of the user's numbers were drawn
matches = 0
for number in user_numbers:
    if number in winning_numbers:
        matches = matches + 1

print(f"The winning numbers are: {winning_numbers}")
print(f"Your numbers are: {user_numbers}")
print(f"You matched {matches} numbers!")
