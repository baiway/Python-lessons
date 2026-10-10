n = int(input("How many rows? "))

# Triangle: row i has i stars
for i in range(1, n + 1):
    row = ""
    for j in range(i):
        row = row + "*"
    print(row)

print()

# Pyramid: row i has (n - i) spaces followed by (2i - 1) stars
for i in range(1, n + 1):
    row = ""
    for j in range(n - i):
        row = row + " "
    for j in range(2*i - 1):
        row = row + "*"
    print(row)
