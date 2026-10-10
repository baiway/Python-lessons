import random

def get_int_in_range(prompt, low, high):
    """Asks the user for a whole number until they enter one between `low`
    and `high` (inclusive), then returns it"""
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("That's not a whole number! Try again.")
            continue

        # `low <= number <= high` is short for `low <= number and number <= high`
        if low <= number <= high:
            return number
        print(f"Please enter a number between {low} and {high}.")


answer = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100...")

guess = get_int_in_range("Your guess: ", 1, 100)
num_guesses = 1

# Keep going until the user guesses correctly, giving hints along the way
while guess != answer:
    if guess > answer:
        print("Too high!")
    else:
        print("Too low!")
    guess = get_int_in_range("Your guess: ", 1, 100)
    num_guesses = num_guesses + 1

print(f"Correct! The answer was {answer}. You took {num_guesses} guesses.")
