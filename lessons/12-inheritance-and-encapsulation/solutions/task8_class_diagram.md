# Task 8 solution (class diagram)
```mermaid
classDiagram
    Car "1" *-- "1" Engine : has
    Car "1" *-- "4" Wheel : has
    Garage "0..1" o-- "*" Car : contains
    class Car {
        registration
        engine
        wheels
        __str__()
    }
    class Engine {
        horsepower
    }
    class Wheel {
        size
    }
    class Garage {
        name
        cars
        park(car)
        remove(car)
        show()
    }
```

- `Car` and `Engine`, and `Car` and `Wheel`, are joined by **composition** (filled diamonds), because the car creates its engine and wheels, and they don't exist on their own. Each car has exactly 1 engine and exactly 4 wheels.
- `Garage` and `Car` are joined by **aggregation** (a hollow diamond), because cars exist independently of garages and can move between them. A garage can hold any number of cars (`*`), and a car is in at most one garage at a time (`0..1`).
