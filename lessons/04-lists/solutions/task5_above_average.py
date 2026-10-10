numbers = []

# Keep asking for numbers until the user types "done"
while True:
    entry = input("Enter a number (or 'done' to finish): ")
    if entry == "done":
        break
    numbers.append(float(entry))

mean = sum(numbers) / len(numbers)

# Collect the numbers that are above the mean
above_mean = []
for number in numbers:
    if number > mean:
        above_mean.append(number)

print(f"You entered {len(numbers)} numbers")
print(f"Their mean is {mean:.2f}")
print(f"The numbers above the mean are: {above_mean}")
