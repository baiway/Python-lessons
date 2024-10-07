# for loop
fav_fruits = ["apples", "pears", "grapes", "bananas", "kiwis"]
for fruit in fav_fruits:
    print(f"I love {fruit}!")

# while loop
import random
ans = random.randint(0, 20)
guess = random.randint(0, 20)
print(f"Trying to guess the random number... (pst... the answer is {ans})")

while ans != guess:
    print(f"Doh! I guessed: {guess}")
    guess = random.randint(0, 20)  # generate another random number
