# `for` loops and `while` loops
When we need to execute code again and again in Python, we can use loops. There are two types of loops in Python: `for` loops and `while` loops. `for` loops will execute a *defined number of times* (e.g. operate on all the elements of a list, or do something 5 times). `while` loops will continue running (potentially indefinitely!) until *some condition* is met. I've included examples of each below.
```python
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
print("Yay, I got it!")
```

The output is shown below.
```
I love apples!
I love pears!
I love grapes!
I love bananas!
I love kiwis!
Trying to guess the random number... (pst... the answer is 0)
Doh! I guessed: 10
Doh! I guessed: 4
Doh! I guessed: 10
Doh! I guessed: 20
Doh! I guessed: 13
Doh! I guessed: 1
Doh! I guessed: 18
Doh! I guessed: 17
Doh! I guessed: 17
Doh! I guessed: 20
Doh! I guessed: 11
Doh! I guessed: 16
Doh! I guessed: 6
Doh! I guessed: 2
Doh! I guessed: 14
Doh! I guessed: 6
Doh! I guessed: 9
Doh! I guessed: 8
Doh! I guessed: 15
Doh! I guessed: 16
Doh! I guessed: 19
Doh! I guessed: 9
Doh! I guessed: 7
Doh! I guessed: 12
Yay! I got it!
```

- [ ] Design a few tasks for students to practice using loops. At least one
      should involve using conditional logic (previous lesson) as well.
