a = [
    [1, 2],
    [3, 4],
]
b = [
    [5, 6],
    [7, 8],
]

# Try replacing `a` and `b` with these to test a 2 x 3 matrix times a 3 x 2
# matrix. The answer should be [[58, 64], [139, 154]].
# a = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
# b = [
#     [7, 8],
#     [9, 10],
#     [11, 12],
# ]

if len(a[0]) != len(b):
    print("These matrices can't be multiplied!")
else:
    # The answer has as many rows as `a` and as many columns as `b`
    product = []
    for i in range(len(a)):
        new_row = []
        for j in range(len(b[0])):
            # Multiply row i of `a` by column j of `b`, item by item, and add up
            total = 0
            for k in range(len(b)):
                total = total + a[i][k] * b[k][j]
            new_row.append(total)
        product.append(new_row)

    for row in product:
        print(row)
