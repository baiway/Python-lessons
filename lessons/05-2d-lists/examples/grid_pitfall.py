# This creates a list containing the SAME row three times...
bad_grid = [[0] * 4] * 3
bad_grid[0][0] = 1
print(bad_grid)  # prints [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]

# ...whereas building each row in a loop creates three separate rows
good_grid = []
for row in range(3):
    new_row = []
    for col in range(4):
        new_row.append(0)
    good_grid.append(new_row)
good_grid[0][0] = 1
print(good_grid)  # prints [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
