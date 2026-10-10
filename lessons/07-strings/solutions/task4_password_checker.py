def is_strong_password(password):
    """Returns `True` if `password` is at least 8 characters long and contains
    an uppercase letter, a lowercase letter and a digit"""
    has_upper = False
    has_lower = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    return len(password) >= 8 and has_upper and has_lower and has_digit


password = input("Choose a password: ")
while not is_strong_password(password):
    print("That password is too weak. It must be at least 8 characters long and")
    print("contain an uppercase letter, a lowercase letter and a digit.")
    password = input("Choose a password: ")
print("Password accepted!")
