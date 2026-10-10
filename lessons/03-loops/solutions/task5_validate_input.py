number = int(input("Enter a number between 1 and 10: "))

# Keep asking until the number is in range
while number < 1 or number > 10:
    print("That number is not between 1 and 10!")
    number = int(input("Enter a number between 1 and 10: "))

print(f"Thanks! You entered {number}")
