# Lesson 3: `for` loops and `while` loops
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
print(f"Trying to guess the random number... (psst... the answer is {ans})")

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
Trying to guess the random number... (psst... the answer is 19)
Doh! I guessed: 12
Doh! I guessed: 4
Doh! I guessed: 16
Doh! I guessed: 4
Doh! I guessed: 9
Yay! I guessed 19
```

As with `if` statements, the line that starts the loop ends with a colon `:`, and the code that is repeated (the _body_ of the loop) is indented. You can find this example in [`examples/loop_examples.py`](examples/loop_examples.py).

## `for` loops and `range`
In the example above, the `for` loop runs once for each item in the list `fav_fruits`. Each time around the loop, the variable `fruit` takes the value of the next item in the list. We'll learn lots more about lists in [Lesson 4](../04-lists).

Very often, we just want to do something a certain number of times, or loop over some numbers. For this we can use `range`:
```python
for i in range(5):
    print(i)
```

which prints:
```
0
1
2
3
4
```

Notice that `range(5)` counts from `0` up to _but not including_ `5`. This catches everyone out at first, but you'll get used to it! `range` can also take a start value and a step size:
- `range(1, 6)` gives `1, 2, 3, 4, 5` (start at 1, stop _before_ 6)
- `range(0, 20, 5)` gives `0, 5, 10, 15` (start at 0, stop before 20, go up in steps of 5)
- `range(10, 0, -1)` gives `10, 9, 8, ..., 1` (count down!)

You can also loop over the characters in a string:
```python
for letter in "hello":
    print(letter)
```

**Task 1:** Use a `for` loop and `range` to:
1. Print the numbers from 1 to 10.
2. Print the even numbers from 2 to 20.
3. Print a countdown from 10 to 1, followed by "Blast off!".

[Solution](solutions/task1_counting.py)

**Task 2:** Write a program that asks the user for a number, then prints its times table from 1 to 12. For example, if the user enters 7, your program should print `1 x 7 = 7`, `2 x 7 = 14`, and so on, up to `12 x 7 = 84`. [Solution](solutions/task2_times_tables.py)

**Task 3:** Write a program that asks the user for a whole number `n` and adds up all the numbers from 1 to `n`. For example, if `n` is 4, then the answer should be $1 + 2 + 3 + 4 = 10$. Hint: create a variable `total = 0` _before_ the loop, then add to it each time around the loop. Check your answer using the formula $\frac{n(n+1)}{2}$. [Solution](solutions/task3_sum_to_n.py)

**Task 4:** Write a program that asks the user to enter a word or sentence, then counts how many vowels it contains. [Solution](solutions/task4_count_vowels.py)

## `while` loops
A `while` loop keeps running for as long as its condition is `True`. Before each time around the loop, Python checks the condition; as soon as it is `False`, the loop stops. For example:
```python
count = 1
while count <= 5:
    print(count)
    count = count + 1  # without this line, the loop would run forever!
```

> [!WARNING]
> If the condition of a `while` loop never becomes `False`, then the loop will run forever. This is called an _infinite loop_. If this happens, press `Ctrl` + `c` in the terminal to stop your program.

`while` loops are particularly useful when you don't know in advance how many times you need to loop. A common example is checking user input: we can keep asking the user for an answer until they give us a valid one.
```python
age = int(input("How old are you? "))
while age < 0 or age > 130:
    print("That can't be right!")
    age = int(input("How old are you? "))
print(f"You are {age} years old.")
```

**Task 5:** Write a program that asks the user to enter a number between 1 and 10. If they enter a number outside this range, keep asking until they enter a valid number. [Solution](solutions/task5_validate_input.py)

**Task 6:** Write a "guess the number" game. The computer should pick a random number between 1 and 100, and the user should keep guessing until they get it right. After each wrong guess, tell the user whether their guess was too high or too low. When they get it right, tell them how many guesses it took. [Solution](solutions/task6_guess_the_number.py)

## `break` and `continue`
Sometimes it's useful to jump out of a loop early, or skip to the next time around the loop. We can do this using `break` and `continue`:
- `break` immediately exits the loop.
- `continue` immediately skips to the next time around the loop.

```python
# Prints 1, 2, 3, 4, then stops
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Prints the odd numbers from 1 to 9
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
```

A common pattern is to use `while True` (a loop that would run forever) together with `break`:
```python
while True:
    answer = input("Do you want to keep going? (yes/no) ")
    if answer == "no":
        break
print("Goodbye!")
```

**Task 7:** _FizzBuzz_ is a classic programming puzzle (it's often used in job interviews!). Write a program that prints the numbers from 1 to 100, except that:
- for multiples of 3, it prints `Fizz` instead of the number,
- for multiples of 5, it prints `Buzz` instead of the number,
- for multiples of both 3 and 5, it prints `FizzBuzz` instead of the number.

[Solution](solutions/task7_fizzbuzz.py)

**Task 8:** Change your rock, paper, scissors program from [Lesson 2](../02-conditionals) so that the user can keep playing until they type `quit`. Keep track of the score and print it at the end. [Solution](solutions/task8_rock_paper_scissors_loop.py)

**⭐ Task 9:** You can put loops inside other loops (these are called _nested_ loops). Use nested loops to write a program that asks the user for a number `n` and prints a triangle of stars with `n` rows. For example, if `n` is 4:
```
*
**
***
****
```

Once you've done this, try to print a pyramid like the one below.
```
   *
  ***
 *****
*******
```

[Solution](solutions/task9_star_patterns.py)

**⭐ Task 10:** A _prime number_ is a whole number greater than 1 that can only be divided exactly by 1 and itself. Write a program that prints all of the prime numbers less than 100. [Solution](solutions/task10_primes.py)

---
[← Previous: Lesson 2](../02-conditionals) | [Contents](../../README.md) | [Next: Lesson 4 →](../04-lists)
