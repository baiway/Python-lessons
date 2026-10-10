def calculate_bmi(mass, height):
    """Calculates body mass index from mass (in kg) and height (in m)"""
    if mass <= 0:
        raise ValueError("Mass must be greater than zero")
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    return mass / height**2
