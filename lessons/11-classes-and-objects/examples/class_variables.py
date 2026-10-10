class Dog:
    species = "Canis familiaris"  # a class variable, shared by all dogs
    num_dogs = 0                  # another class variable

    def __init__(self, name, age):
        self.name = name          # instance variables: each dog has its own
        self.age = age
        Dog.num_dogs = Dog.num_dogs + 1

    @staticmethod
    def human_years(dog_years):
        """Converts a dog's age into (very roughly!) human years"""
        return dog_years * 7

    @classmethod
    def from_string(cls, text):
        """Creates a dog from a string like "Rex,3" """
        name, age = text.split(",")
        return cls(name, int(age))


rex = Dog("Rex", 3)
fido = Dog("Fido", 7)
print(Dog.num_dogs)   # prints 2
print(rex.species)    # Python looks for `species` on rex, then on the Dog class

# A static method doesn't need an object
print(Dog.human_years(3))

# A class method gives us another way of creating objects
bella = Dog.from_string("Bella,5")
print(bella.name, bella.age, Dog.num_dogs)

# The common bug: assigning using an object creates a NEW instance variable
rex.num_dogs = 100
print(rex.num_dogs, fido.num_dogs, Dog.num_dogs)  # prints 100 3 3
