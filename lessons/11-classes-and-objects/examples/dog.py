class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def birthday(self):
        self.age = self.age + 1
        print(f"Happy birthday, {self.name}! You are now {self.age}.")

    def __str__(self):
        return f"{self.name} ({self.age} years old)"


# Create two separate Dog objects
rex = Dog("Rex", 3)
fido = Dog("Fido", 7)

rex.bark()
fido.bark()
rex.birthday()
print(fido.age)  # Fido's age hasn't changed
print(rex)       # uses `__str__`

# Objects can be stored in lists, just like any other value
dogs = [rex, fido, Dog("Bella", 5)]

oldest = dogs[0]
for dog in dogs:
    if dog.age > oldest.age:
        oldest = dog

print(f"The oldest dog is {oldest}")
