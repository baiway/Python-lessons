def get_int(prompt):
    """Keeps asking the user for a whole number until they enter one"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a whole number! Try again.")


a = get_int("Enter a whole number: ")
b = get_int("Enter another whole number: ")
print(f"{a} + {b} = {a + b}")
