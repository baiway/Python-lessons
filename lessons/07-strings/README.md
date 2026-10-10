# Lesson 7: Strings and string formatting
We've been using strings since our very first program, but there's a lot more to them than we've seen so far. In this lesson, we'll learn how to pick strings apart, how to use some of their many built-in methods, and how to format output exactly the way we want it.

## Strings are sequences
A string is a _sequence_ of characters, and in many ways it behaves just like a list of characters. You can find its length with `len`, pick out individual characters by indexing, take slices, loop over it, and check whether it contains something using `in`:
```python
>>> word = "Python"
>>> len(word)
6
>>> word[0]
'P'
>>> word[-1]
'n'
>>> word[1:4]
'yth'
>>> word[::-1]
'nohtyP'
>>> "th" in word
True
```

There's one important difference though: strings are _immutable_, which means they can't be changed once they've been created. If you try to change a character, you'll get an error:
```python
>>> word[0] = "J"
TypeError: 'str' object does not support item assignment
```

Instead, you have to create a new string. For example, `word = "J" + word[1:]` creates the new string `"Jython"` and stores it in `word`.

You can join strings together (_concatenate_ them) using `+`, and repeat them using `*`:
```python
>>> "Hello" + " " + "world"
'Hello world'
>>> "ha" * 3
'hahaha'
```

**Task 1:** Write a program that asks the user for their first name and their surname, then prints: [Solution](solutions/task1_name_slicing.py)
1. Their initials (e.g. `A.L.` for Ada Lovelace).
2. Their full name in reverse (e.g. `ecalevoL adA`).
3. The number of letters in their full name, not counting the space.
4. The first three letters of their surname.

**Task 2:** A _palindrome_ is a word that reads the same forwards and backwards, like "racecar" or "level". Write a function `is_palindrome(text)` that returns `True` if `text` is a palindrome. Then improve it so that it ignores capital letters and spaces, so that phrases like "Never odd or even" count as palindromes too. [Solution](solutions/task2_palindromes.py)

## String methods
Like lists, strings have lots of built-in methods. Because strings are immutable, none of these change the original string; instead, they give you back a new one. Here are some of the most useful:

| Method                | What it does                                                    | Example                         | Result              |
|-----------------------|-----------------------------------------------------------------|---------------------------------|---------------------|
| `.upper()`            | Converts to UPPERCASE                                           | `"Hello".upper()`               | `'HELLO'`           |
| `.lower()`            | Converts to lowercase                                           | `"Hello".lower()`               | `'hello'`           |
| `.title()`            | Capitalises The First Letter Of Each Word                       | `"ada lovelace".title()`        | `'Ada Lovelace'`    |
| `.strip()`            | Removes spaces (and new lines) from the start and end           | `"  hi  ".strip()`              | `'hi'`              |
| `.replace(old, new)`  | Replaces every `old` with `new`                                 | `"cat".replace("c", "b")`       | `'bat'`             |
| `.split()`            | Splits into a list of words                                     | `"a b c".split()`               | `['a', 'b', 'c']`   |
| `.split(sep)`         | Splits into a list wherever `sep` appears                       | `"a,b,c".split(",")`            | `['a', 'b', 'c']`   |
| `sep.join(list)`      | Joins a list of strings together, with `sep` between each one   | `"-".join(["a", "b", "c"])`     | `'a-b-c'`           |
| `.find(sub)`          | Gives the index of the first `sub`, or `-1` if it isn't there   | `"banana".find("n")`            | `2`                 |
| `.count(sub)`         | Counts how many times `sub` appears                             | `"banana".count("a")`           | `3`                 |
| `.startswith(sub)`    | Checks whether the string starts with `sub`                     | `"Python".startswith("Py")`     | `True`              |
| `.isdigit()`          | Checks whether every character is a digit                       | `"123".isdigit()`               | `True`              |
| `.isalpha()`          | Checks whether every character is a letter                      | `"abc1".isalpha()`              | `False`             |
| `.isupper()`          | Checks whether every letter is uppercase                        | `"ABC".isupper()`               | `True`              |

Notice that `.split()` and `.join()` are opposites: `split` turns a string into a list, and `join` turns a list back into a string. These are particularly useful when reading data from files, which we'll do in [Lesson 9](../09-files).

**Task 3:** Many schools create usernames for their students by combining the first three letters of the student's surname, their first initial, and the last two digits of the year they joined, all in lowercase. For example, Ada Lovelace joining in 2026 would get the username `lova26`. Write a function `make_username(first_name, surname, year)` that returns the username, and test it on a few names. Make sure it still works if the user types their name with extra spaces or in capitals. [Solution](solutions/task3_usernames.py)

**Task 4:** Write a function `is_strong_password(password)` that returns `True` only if the password is at least 8 characters long and contains at least one uppercase letter, at least one lowercase letter and at least one digit. Use it to keep asking the user for a password until they enter a strong one. [Solution](solutions/task4_password_checker.py)

**Task 5:** Write a program that asks the user for a sentence, then prints: the number of words, the longest word, and the mean word length. Hint: use `.split()`. [Solution](solutions/task5_word_stats.py)

## Characters and character codes
Computers store everything as numbers, including text. Each character is stored as a number called its _character code_. Python uses a system called _Unicode_, whose first 128 codes are the same as an older system called _ASCII_. You can convert between characters and their codes using `ord` and `chr`:
```python
>>> ord("A")
65
>>> ord("a")
97
>>> chr(66)
'B'
>>> chr(ord("A") + 2)
'C'
```

Notice that the uppercase letters `A` to `Z` have codes 65 to 90, one after another, and the lowercase letters `a` to `z` have codes 97 to 122. This makes it easy to "shift" letters along the alphabet.

**Task 6:** A _Caesar cipher_ is one of the oldest ways of encrypting a message: each letter is shifted a fixed number of places along the alphabet, wrapping around from Z back to A. For example, with a shift of 3, `A` becomes `D`, `B` becomes `E`, and `Z` becomes `C`. Write a function `caesar_encrypt(message, shift)` that encrypts a message (leaving spaces and punctuation unchanged), and a function `caesar_decrypt(message, shift)` that decrypts it. Hint: you'll need `ord`, `chr`, and `%`. [Solution](solutions/task6_caesar_cipher.py)

## Escape characters and multi-line strings
Some characters are hard to type inside a string, so we write them using a backslash `\` followed by another character. These are called _escape characters_. The most common are:
- `\n`: a new line
- `\t`: a tab
- `\"` and `\'`: a quotation mark (useful if your string is surrounded by the same type of quotation mark)
- `\\`: a backslash

```python
>>> print("Line one\nLine two")
Line one
Line two
>>> print("She said \"hello\"")
She said "hello"
```

You can also write a string over several lines by surrounding it with triple quotes (`"""` or `'''`). This is how docstrings work!

## Formatting with f-strings
We met f-strings in [Lesson 1](../01-variables-and-types), and we've already seen a couple of _format specifiers_: `:.2f` to round to 2 decimal places, and `:4` to make something take up 4 characters. There are many more, and they can be combined. The general form is `{value:fill align width , .precision type}`, where every part is optional. This sounds complicated, but the examples below should make it clearer.

| Specifier    | Meaning                                              | Example                       | Result          |
|--------------|------------------------------------------------------|-------------------------------|-----------------|
| `:.2f`       | 2 decimal places                                     | `f"{3.14159:.2f}"`            | `'3.14'`        |
| `:8`         | Take up (at least) 8 characters                      | `f"{42:8}"`                   | `'      42'`    |
| `:<8`        | Left-align in 8 characters                           | `f"{'hi':<8}"`                | `'hi      '`    |
| `:>8`        | Right-align in 8 characters                          | `f"{'hi':>8}"`                | `'      hi'`    |
| `:^8`        | Centre in 8 characters                               | `f"{'hi':^8}"`                | `'   hi   '`    |
| `:*^8`       | Centre in 8 characters, filling the gaps with `*`    | `f"{'hi':*^8}"`               | `'***hi***'`    |
| `:05`        | Pad with zeros to 5 characters                       | `f"{42:05}"`                  | `'00042'`       |
| `:,`         | Separate thousands with commas                       | `f"{1234567:,}"`              | `'1,234,567'`   |
| `:.1%`       | Show as a percentage, to 1 decimal place             | `f"{0.256:.1%}"`              | `'25.6%'`       |
| `:>10.2f`    | Right-align in 10 characters, to 2 decimal places    | `f"{3.14159:>10.2f}"`         | `'      3.14'`  |

By default, numbers are right-aligned and strings are left-aligned. One more handy trick: putting `=` after an expression prints the expression _and_ its value, which is great for debugging:
```python
>>> x = 7
>>> print(f"{x=}, {x**2=}")
x=7, x**2=49
```

> [!NOTE]
> You may see older Python code that formats strings using `.format()` (e.g. `"Hello, {}!".format(name)`) or the `%` operator (e.g. `"Hello, %s!" % name`). These still work, and use similar format specifiers, but f-strings are generally easier to read.

**Task 7:** Write a program that prints a neatly formatted receipt for the shopping basket below. The item names should be left-aligned, the quantities centred and the prices right-aligned, with every price shown to 2 decimal places. Finish the receipt with the total. [Solution](solutions/task7_receipt.py)
```python
items = ["Bread", "Milk", "Cheddar cheese", "Apples"]
quantities = [1, 2, 1, 6]
prices = [1.35, 0.95, 3.50, 0.30]  # price of a single item, in £
```

Your output should look something like this:
```
==========================================
Item                  Qty            Price
------------------------------------------
Bread                  1             £1.35
Milk                   2             £1.90
Cheddar cheese         1             £3.50
Apples                 6             £1.80
------------------------------------------
Total                                £8.55
==========================================
```

**⭐ Task 8:** _Run-length encoding_ (RLE) is a simple way of compressing data that contains lots of repeated characters. Each run of repeated characters is replaced by the number of times it repeats, followed by the character. For example, `"AAAABBBCCD"` becomes `"4A3B2C1D"`. Write a function `rle_encode(text)` that compresses a string using RLE, and a function `rle_decode(text)` that decompresses it again. You can assume that the original text doesn't contain any digits. Make sure your decoder can handle runs of 10 or more! [Solution](solutions/task8_run_length_encoding.py)

**⭐ Task 9:** Two words are _anagrams_ if they contain exactly the same letters, e.g. "listen" and "silent". Write a function `are_anagrams(word1, word2)` that checks whether two words are anagrams, ignoring capital letters and spaces. Can you think of two different ways of doing this? [Solution](solutions/task9_anagrams.py)

---
[← Previous: Lesson 6](../06-functions) | [Contents](../../README.md) | [Next: Lesson 8 →](../08-exceptions)
