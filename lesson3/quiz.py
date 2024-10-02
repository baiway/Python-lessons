import random

# Get get limits from user
print("Please enter the lower and upper limit.")
lower_lim = int(input("Lower limit: "))
upper_lim = int(input("Upper limit: "))

# Generate `num1` and `num2`
num1 = random.randint(lower_lim, upper_lim)
num2 = random.randint(lower_lim, upper_lim)

answer = 2*num1 + num2
user_ans = int(input(f"What is 2*{num1} + {num2}? "))

# Check whether user is correct
if user_ans == answer:
    print(f"You are correct! The answer is: {answer}")
else:
    print(f"WRONG! The answer is: {answer}")
