grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# 1. The middle number
print(grid[1][1])

# 2. The four corners
print(grid[0][0], grid[0][2], grid[2][0], grid[2][2])

# 3. The bottom row
print(grid[2])  # or grid[-1]

# 4. The middle column: pick out the item at index 1 from each row
middle_column = []
for row in grid:
    middle_column.append(row[1])
print(middle_column)
