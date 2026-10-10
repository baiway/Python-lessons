ABSOLUTE_ZERO = -273.15  # in degrees Celsius


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  # this uses the setter, so it's checked too

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < ABSOLUTE_ZERO:
            raise ValueError(f"Temperatures can't be below absolute zero ({ABSOLUTE_ZERO} °C)")
        self._celsius = value

    @property
    def fahrenheit(self):
        return 9/5 * self._celsius + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        # Convert to Celsius, and use the `celsius` setter so the value is checked
        self.celsius = 5/9 * (value - 32)


t = Temperature(100)
print(t.fahrenheit)  # 212.0
t.fahrenheit = 32
print(t.celsius)     # 0.0

try:
    t.celsius = -300
except ValueError as error:
    print(f"Error: {error}")

try:
    t.fahrenheit = -500
except ValueError as error:
    print(f"Error: {error}")
