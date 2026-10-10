# Lesson 5: 2D lists
In [Lesson 4](../04-lists), we saw that lists can contain any type of value. That includes _other lists_! A list of lists is called a _2D list_ (or sometimes a 2D array, a grid, a table or a matrix). They're very useful for storing anything that has rows and columns: game boards, seating plans, spreadsheets, images, and so on.

## Creating and indexing 2D lists
Here is a 2D list representing a 3 × 3 grid of numbers. I've written each row on its own line to make it easier to read, but Python doesn't mind how you lay it out.
```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

`grid` is a list with three items, and each item is itself a list (a _row_). So `grid[0]` gives us the first row, and `grid[0][2]` gives us the item at index `2` _within_ the first row:
```python
>>> grid[0]
[1, 2, 3]
>>> grid[0][2]
3
>>> grid[2][0]
7
```

The general rule is `grid[row][column]`: the first index picks the row, and the second picks the column. As with ordinary lists, both indexes start at `0`. We can change an item in the same way:
```python
>>> grid[1][1] = 0
>>> grid
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
```

The number of rows is `len(grid)`, and the number of columns is the length of any one row, e.g. `len(grid[0])`.

**Task 1:** Using the `grid` above (before it was changed), write a program that prints: [Solution](solutions/task1_grid_indexing.py)
1. The middle number (`5`).
2. The four corners.
3. The whole of the bottom row.
4. The whole of the middle _column_. Hint: there is no shortcut for this -- you'll need to pick out one item from each row.

## Looping over 2D lists
To visit every item in a 2D list, we use _nested_ loops (which we first saw in [Lesson 3](../03-loops)): an outer loop that goes through each row, and an inner loop that goes through each item in that row.
```python
for row in grid:
    for item in row:
        print(item, end=" ")
    print()  # start a new line at the end of each row
```

which prints:
```
1 2 3
4 5 6
7 8 9
```

Notice that we've given `print` an extra argument, `end=" "`. Normally, `print` puts a new line at the end of whatever it prints. `end=" "` tells it to put a space there instead, so that all the items in a row appear on the same line. An empty `print()` then just prints a new line.

If you need the row and column indexes, loop over `range(len(grid))` and `range(len(grid[row]))` instead:
```python
for row in range(len(grid)):
    for col in range(len(grid[row])):
        print(f"grid[{row}][{col}] = {grid[row][col]}")
```

When printing tables of numbers, it's useful to make every number take up the same amount of space so that the columns line up. We can do this with an f-string by putting a width after a colon: `f"{x:4}"` makes `x` take up 4 characters. We'll see more of these _format specifiers_ in [Lesson 7](../07-strings).

**Task 2:** Use nested loops to print a 12 × 12 multiplication grid, like the one below (only the first few rows are shown). Make sure the columns line up! [Solution](solutions/task2_times_table_grid.py)
```
   1   2   3   4   5   6   7   8   9  10  11  12
   2   4   6   8  10  12  14  16  18  20  22  24
   3   6   9  12  15  18  21  24  27  30  33  36
```

## Creating 2D lists with loops
Sometimes we need to make a 2D list of a particular size, filled with some starting value. The safest way to do this is to build each row inside a loop:
```python
num_rows = 3
num_cols = 4

grid = []
for row in range(num_rows):
    new_row = []
    for col in range(num_cols):
        new_row.append(0)
    grid.append(new_row)
```

> [!WARNING]
> You may see people create a 2D list using `grid = [[0] * 4] * 3`. **Don't do this!** It looks like it works, but it actually creates a list containing _the same row three times_ (remember the section on copying lists in [Lesson 4](../04-lists)?). Changing `grid[0][0]` will change the first item in _every_ row. Try it in interactive mode and see! You can find this example in [`examples/grid_pitfall.py`](examples/grid_pitfall.py).

## Tables of data
2D lists are also a natural way to store tables of data, where each row is a record (e.g. a student) and each column is a field (e.g. their score in a test). For example, the table below stores the scores of four students in three tests.
```python
names = ["Ada", "Alan", "Grace", "Tim"]
scores = [
    [72, 85, 64],  # Ada
    [90, 78, 88],  # Alan
    [65, 70, 71],  # Grace
    [81, 93, 77],  # Tim
]
```

**Task 3:** Using `names` and `scores` above, write a program that prints [Solution](solutions/task3_test_scores.py)
1. Each student's mean score (the mean of each _row_).
2. The mean score for each test (the mean of each _column_).
3. The name of the student with the highest mean score.

**Task 4:** In maths, a 2D grid of numbers is called a _matrix_. To add two matrices of the same size, you add together the numbers in the same positions. Write a program that adds the two matrices below, storing the answer in a new 2D list, and prints the result one row at a time. [Solution](solutions/task4_matrix_addition.py)
```python
a = [
    [1, 2, 3],
    [4, 5, 6],
]
b = [
    [10, 20, 30],
    [40, 50, 60],
]
```

**Task 5:** Write a two-player game of noughts and crosses. Use the starter code in [`exercises/noughts_and_crosses.py`](exercises/noughts_and_crosses.py) to start you off. Your game should: [Solution](solutions/task5_noughts_and_crosses.py)
1. Print the board before each turn.
2. Ask the current player for a row and a column (each between 0 and 2).
3. If that square is already taken, tell the player and ask again.
4. Swap between players `X` and `O` after each valid move.
5. Stop when the board is full.

**⭐ Task 6:** Improve your noughts and crosses game so that it checks whether a player has won after each move. A player wins if they have three in a row horizontally, vertically or diagonally. Print a message saying who won, and end the game straight away. [Solution](solutions/task6_noughts_and_crosses_winner.py)

**⭐ Task 7:** To multiply two matrices $A$ and $B$, the item in row $i$ and column $j$ of the answer is found by multiplying each item in row $i$ of $A$ by the matching item in column $j$ of $B$, and adding them all up. For example:

```math
\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
\begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}
=
\begin{pmatrix} 1 \times 5 + 2 \times 7 & 1 \times 6 + 2 \times 8 \\ 3 \times 5 + 4 \times 7 & 3 \times 6 + 4 \times 8 \end{pmatrix}
=
\begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}
```

Write a program that multiplies two matrices. It should work for any sizes of matrices that can be multiplied (the number of columns in $A$ must equal the number of rows in $B$). Test it on the example above, then on a 2 × 3 matrix multiplied by a 3 × 2 matrix. [Solution](solutions/task7_matrix_multiplication.py)

---
[← Previous: Lesson 4](../04-lists) | [Contents](../../README.md) | [Next: Lesson 6 →](../06-functions)
