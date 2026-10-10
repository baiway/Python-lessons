def get_int_in_range(prompt, low, high):
    """Asks the user for a whole number until they enter one between `low`
    and `high` (inclusive), then returns it"""
    number = int(input(prompt))
    while number < low or number > high:
        print(f"Please enter a number between {low} and {high}.")
        number = int(input(prompt))
    return number


age = get_int_in_range("How old are you? ", 0, 120)
fav_number = get_int_in_range("What is your favourite number from 1 to 10? ", 1, 10)
print(f"You are {age} years old and your favourite number is {fav_number}.")
