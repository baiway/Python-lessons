# Lesson 9: Reading and writing files
So far, all of our programs have forgotten everything as soon as they finish running. If we want to keep data between runs (e.g. a high score table), or work with data that already exists (e.g. a spreadsheet of exam results), we need to read from and write to _files_. In this lesson, we'll work with _text files_: files that contain plain text, like `.txt` and `.csv` files (and, in fact, `.py` files!).

## Where does Python look for files?
When you open a file by name, e.g. `poem.txt`, Python looks for it in the _current working directory_. This is the folder your terminal is in when you run your program, which isn't necessarily the folder your program is saved in!

For this lesson, the simplest thing to do is to save each data file **in the same folder as your program**, open that folder in VS Code (using "File" → "Open Folder..."), and run your program from the terminal with `python <script>.py`. If you get a `FileNotFoundError` even though the file definitely exists, the current working directory is almost certainly the problem. You can check which folder your terminal is in by typing `pwd` (macOS/Linux/PowerShell), and move into the right folder using `cd <folder name>`.

The data files for this lesson are in the [`data`](data) folder. To download one from GitHub, click on it, then click the "Download raw file" button (a downward-pointing arrow, top-right).

## Reading files
To read a file, we first _open_ it using `open`, then read its contents. The best way to do this is with a `with` statement:
```python
with open("poem.txt", encoding="utf-8") as file:
    contents = file.read()

print(contents)
```

There are a few things to notice here:
1. `open("poem.txt", ...)` opens the file and gives us a _file object_, which we store in the variable `file`. We can then use this to read the file's contents.
2. The `with` statement automatically _closes_ the file when the indented block finishes, even if an exception happens. Closing files is important: it frees up resources, and makes sure anything you've written actually gets saved. (You might remember from [Lesson 8](../08-exceptions) that this is the kind of job `finally` was designed for. `with` does it for you, which is why you'll rarely need `finally`.)
3. `encoding="utf-8"` tells Python how the text in the file is stored. You can usually leave this out on macOS and Linux, but on Windows, leaving it out can cause errors (or garbled text) if the file contains anything other than plain English letters, like `£` or `é`. It's a good habit to always include it.

`file.read()` gives us the whole file as a single string. More often, we want to deal with a file one line at a time. We can do this by looping over the file object:
```python
with open("poem.txt", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

Each `line` includes the new line character `\n` at the end, so we usually remove it with `.strip()`. (Try removing `.strip()` to see what happens!) Alternatively, `file.readlines()` gives you a list of all the lines in the file.

You can find these examples in [`examples/reading_files.py`](examples/reading_files.py).

**Task 1:** Download [`poem.txt`](data/poem.txt) and save it in the same folder as your program. Write a program that prints each line of the poem with its line number, like the output below. Hint: `enumerate` can take a second argument, `start`, which sets the number it starts counting from. [Solution](solutions/task1_line_numbers.py)
```
1: Who has seen the wind?
2: Neither I nor you:
...
```

## Writing files
To write to a file, we pass a second argument to `open`, called the _mode_. The most common modes are:

| Mode  | Name   | What it does                                                                         |
|-------|--------|--------------------------------------------------------------------------------------|
| `"r"` | Read   | Opens a file for reading. This is the default if you don't give a mode.              |
| `"w"` | Write  | Opens a file for writing. Creates the file if it doesn't exist, and **deletes everything in it** if it does! |
| `"a"` | Append | Opens a file for writing, adding to the end of it. Creates the file if it doesn't exist. |

We can then write to the file using `file.write`. Unlike `print`, `write` doesn't add a new line at the end, so you need to add `\n` yourself:
```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("eggs\n")
    file.write("milk\n")
    file.write("bread\n")
```

You can find this example in [`examples/writing_files.py`](examples/writing_files.py).

> [!WARNING]
> Opening a file in `"w"` mode deletes its contents straight away, before you've written anything. Be very careful not to open a file you care about in `"w"` mode by accident!

**Task 2:** Write a program that asks the user for their five favourite films and writes them to a file called `films.txt`, one per line. Then write a second program that reads `films.txt` and prints the films as a numbered list. [Solution (writing)](solutions/task2_write_films.py) | [Solution (reading)](solutions/task2_read_films.py)

**Task 3:** Write a "diary" program that asks the user how their day went, then adds their answer to the end of a file called `diary.txt`, along with today's date. Run it a few times and check that the old entries are still there. Hint: you can get today's date as a string using the code below. [Solution](solutions/task3_diary.py)
```python
import datetime

today = str(datetime.date.today())  # e.g. "2026-10-10"
```

## CSV files
A _CSV_ (comma-separated values) file stores a table of data as plain text. Each line is a row, and the values in each row are separated by commas. You can open CSV files in spreadsheet programs like Excel, but because they're just text, they're also easy to read in Python. For example, [`scores.csv`](data/scores.csv) looks like this:
```
Ada,72
Alan,90
Grace,65
Tim,81
```

To read it, we loop over the lines, use `.split(",")` to split each line into a list of values, and convert the values to the right types (everything we read from a file is a string, just like with `input`!):
```python
names = []
scores = []
with open("scores.csv", encoding="utf-8") as file:
    for line in file:
        values = line.strip().split(",")
        names.append(values[0])
        scores.append(int(values[1]))
```

To write a CSV file, we do the opposite: join the values together with commas (converting them to strings first), and add a `\n` at the end of each line:
```python
with open("new_scores.csv", "w", encoding="utf-8") as file:
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
```

You can find these examples in [`examples/csv_files.py`](examples/csv_files.py).

**Task 4:** Download [`scores.csv`](data/scores.csv). Write a program that reads it and prints each student's name and score, followed by the mean score and the name of the student with the highest score. [Solution](solutions/task4_read_scores.py)

**Task 5:** [`high_scores.csv`](data/high_scores.csv) stores the top 5 scores for a game, from highest to lowest. Write a program that: [Solution](solutions/task5_high_scores.py)
1. Reads the high scores into a 2D list (each row should be `[name, score]`).
2. Asks the user for a new player's name and score.
3. Inserts the new score in the correct position, so the list stays in order.
4. Keeps only the top 5 scores.
5. Writes the new high score table back to `high_scores.csv`, and prints it.

**Task 6:** Write a program that asks the user for the name of a file, then prints how many lines, words and characters it contains. If the file doesn't exist, your program should print a helpful message instead of crashing. Test it on [`poem.txt`](data/poem.txt) and on a file that doesn't exist. [Solution](solutions/task6_file_stats.py)

**Task 7:** [`weather.csv`](data/weather.csv) contains the maximum and minimum temperatures in a town over two weeks. Unlike `scores.csv`, its first line is a _header_ that says what each column contains. Write a program that skips the header, works out the hottest day, the coldest night and the mean maximum temperature, and writes a short summary to a new file called `weather_summary.txt`. Hint: `next(file)` reads one line from a file, so you can use it to skip the header. [Solution](solutions/task7_weather.py)

**⭐ Task 8:** Copy your `caesar_encrypt` and `caesar_decrypt` functions from [Lesson 7](../07-strings) Task 6. Write a program that reads [`message.txt`](data/message.txt), encrypts it with a shift of your choice, and writes the result to `encrypted.txt`. Then write a second program that decrypts `encrypted.txt` and prints the result. [Solution (encrypting)](solutions/task8_encrypt_file.py) | [Solution (decrypting)](solutions/task8_decrypt_file.py)

**⭐ Task 9:** Look at [`people.csv`](data/people.csv). Some of the values contain commas, so they've been surrounded by quotation marks. What goes wrong if you read this file using `.split(",")`? Python's built-in `csv` module knows how to deal with this. Look up how to use `csv.reader` in the [Python documentation](https://docs.python.org/3/library/csv.html), and use it to print each person's name and favourite food correctly. [Solution](solutions/task9_csv_module.py)

---
[← Previous: Lesson 8](../08-exceptions) | [Contents](../../README.md) | [Next: Lesson 10 →](../10-searching-and-sorting)
