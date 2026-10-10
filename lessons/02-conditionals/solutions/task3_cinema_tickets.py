age = int(input("How old are you? "))

if age < 12 or age >= 65:
    price = 5
else:
    price = 9

print(f"Your ticket costs £{price}")
