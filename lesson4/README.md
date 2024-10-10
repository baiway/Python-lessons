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
print(f"Yay! I guessed {guess}")
```

The output is shown below.
```
I love apples!
I love pears!
I love grapes!
I love bananas!
I love kiwis!
Trying to guess the random number... (pst... the answer is 19)
Doh! I guessed: 12
Doh! I guessed: 4
Doh! I guessed: 16
Doh! I guessed: 4
Doh! I guessed: 9
Yay! I guessed 19
```

- [ ] Design a few tasks for students to practice using loops. At least one
      should involve using conditional logic (previous lesson) as well.
