import random

answer = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100...")

guess = int(input("Your guess: "))
num_guesses = 1

# Keep going until the user guesses correctly, giving hints along the way
while guess != answer:
    if guess > answer:
        print("Too high!")
    else:
        print("Too low!")
    guess = int(input("Your guess: "))
    num_guesses = num_guesses + 1

print(f"Correct! The answer was {answer}. You took {num_guesses} guesses.")
