class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # this calls the setter below!

    @property
    def age(self):
        """The getter: called when you read `person.age`"""
        return self._age

    @age.setter
    def age(self, value):
        """The setter: called when you write `person.age = value`"""
        if value < 0:
            raise ValueError("Age can't be negative")
        self._age = value


ada = Person("Ada", 36)
print(ada.age)  # calls the getter
ada.age = 37    # calls the setter
print(ada.age)

try:
    ada.age = -5  # calls the setter, which raises a ValueError
except ValueError as error:
    print(f"Error: {error}")
