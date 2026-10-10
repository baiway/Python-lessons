import random

# Get limits from user
print("Please enter the lower and upper limit.")
lower_lim = int(input("Lower limit: "))
upper_lim = ...

# Generate `num1` and `num2`
num1 = random.randint(lower_lim, upper_lim)
num2 = ...

answer = num1 * num2  # feel free to change this to anything you like
user_ans = int(input(f"What is {num1} * {num2}? "))

# Check whether user is correct
if ...:
    print(f"You are correct! The answer is: {answer}")
else:
    print(f"WRONG! The answer is: {answer}")
