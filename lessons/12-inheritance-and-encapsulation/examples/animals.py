class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping. Zzz...")

    def speak(self):
        print(f"{self.name} makes a noise.")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def __init__(self, name, indoor):
        super().__init__(name)
        self.indoor = indoor

    def speak(self):
        print(f"{self.name} says: Meow!")


rex = Dog("Rex")
rex.sleep()  # inherited from Animal
rex.speak()  # overridden in Dog

print(isinstance(rex, Dog))     # True
print(isinstance(rex, Animal))  # True: a dog is an animal
print(isinstance(rex, Cat))     # False

# Polymorphism: each animal uses its own version of `speak`
animals = [Dog("Rex"), Cat("Tom", indoor=True), Dog("Fido")]
for animal in animals:
    animal.speak()
