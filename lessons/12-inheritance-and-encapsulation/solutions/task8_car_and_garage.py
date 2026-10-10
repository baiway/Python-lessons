class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Wheel:
    def __init__(self, size):
        self.size = size  # in inches


class Car:
    def __init__(self, registration, horsepower, wheel_size):
        self.registration = registration
        # Composition: the car creates its own engine and wheels, which belong
        # to it and nothing else
        self.engine = Engine(horsepower)
        self.wheels = []
        for i in range(4):
            self.wheels.append(Wheel(wheel_size))

    def __str__(self):
        return f"{self.registration} ({self.engine.horsepower} hp, {self.wheels[0].size}\" wheels)"


class Garage:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def park(self, car):
        # Aggregation: the cars exist independently, and are passed in
        self.cars.append(car)

    def remove(self, car):
        self.cars.remove(car)

    def show(self):
        print(f"{self.name}:")
        for car in self.cars:
            print(f"  {car}")


home = Garage("Home")
work = Garage("Work")

mini = Car("AB12 CDE", 134, 16)
tesla = Car("EV24 ZAP", 283, 18)

home.park(mini)
home.park(tesla)
home.show()

# Move a car from one garage to another: the car itself isn't affected
home.remove(tesla)
work.park(tesla)
home.show()
work.show()
