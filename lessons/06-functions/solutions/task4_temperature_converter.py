def celsius_to_fahrenheit(c):
    """Converts a temperature from degrees Celsius to degrees Fahrenheit"""
    return 9/5 * c + 32


def fahrenheit_to_celsius(f):
    """Converts a temperature from degrees Fahrenheit to degrees Celsius"""
    return 5/9 * (f - 32)


print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Which conversion would you like to do? ")

temperature = float(input("Enter the temperature: "))
if choice == "1":
    print(f"{temperature} °C is {celsius_to_fahrenheit(temperature):.1f} °F")
elif choice == "2":
    print(f"{temperature} °F is {fahrenheit_to_celsius(temperature):.1f} °C")
else:
    print("Please choose either 1 or 2")
