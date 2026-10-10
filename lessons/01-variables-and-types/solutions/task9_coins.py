amount = int(input("Enter an amount in pence: "))
print(f"The fewest coins needed to make {amount}p are:")

# Work from the biggest coin down. At each step, `//` tells us how many
# of that coin we need, and `%` tells us how much is left over.
two_pounds = amount // 200
amount = amount % 200

one_pounds = amount // 100
amount = amount % 100

fifty_pences = amount // 50
amount = amount % 50

twenty_pences = amount // 20
amount = amount % 20

ten_pences = amount // 10
amount = amount % 10

five_pences = amount // 5
amount = amount % 5

two_pences = amount // 2
amount = amount % 2

one_pences = amount  # whatever is left must be made of 1p coins

print(f"  £2: {two_pounds}")
print(f"  £1: {one_pounds}")
print(f"  50p: {fifty_pences}")
print(f"  20p: {twenty_pences}")
print(f"  10p: {ten_pences}")
print(f"  5p: {five_pences}")
print(f"  2p: {two_pences}")
print(f"  1p: {one_pences}")
