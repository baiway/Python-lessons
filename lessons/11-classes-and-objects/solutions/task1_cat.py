class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def meow(self):
        print(f"{self.name} the {self.colour} cat says: Meow!")


tom = Cat("Tom", "grey")
felix = Cat("Felix", "black")
garfield = Cat("Garfield", "ginger")

tom.meow()
felix.meow()
garfield.meow()
