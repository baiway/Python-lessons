a = [
    [1, 2, 3],
    [4, 5, 6],
]
b = [
    [10, 20, 30],
    [40, 50, 60],
]

# Add the items in matching positions, building the answer one row at a time
total = []
for row in range(len(a)):
    new_row = []
    for col in range(len(a[row])):
        new_row.append(a[row][col] + b[row][col])
    total.append(new_row)

for row in total:
    print(row)
