def calculate_bmi(mass, height):
    """Calculates body mass index from mass (in kg) and height (in m)"""
    if mass <= 0:
        raise ValueError("Mass must be greater than zero")
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    return mass / height**2


try:
    mass = float(input("Enter your mass in kilograms: "))
    height = float(input("Enter your height in metres: "))
    bmi = calculate_bmi(mass, height)
    print(f"Your BMI is {bmi:.1f}")
except ValueError as error:
    # This catches both invalid numbers (from `float`) and the errors raised
    # by `calculate_bmi`
    print(f"Error: {error}")
