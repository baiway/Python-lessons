# Data types and variables in Python
## Variables
We can use the assignment operator `=` to store values in variables. For example:
```python
>>> x = 3
>>> y = x**2 + 3*x - 9
>>> print(x)
3
>>> print(y)
9
```

**Task 1:** Determine the area of a triangle with a base length of 6 cm and a height of 9 cm. Store the lengths as variables `base` and `height` then use the formula `area = 0.5 * base * height` to calculate the area. Print the result to the screen using `print(area)`.

**Task 2:** The surface area $s$ of an octohedron with side length $a$ is $s = 2a^2 \sqrt{3}$. Determine the surface area of an octohedron with side length 8 cm.

## Data types
Some of the basic data types in Python at listed below. There are more types (for a complete list, click [here](https://docs.python.org/3/library/stdtypes.html)), and it's even possible to define your own, but these will be enough for our purposes for a while.

|   Class  |        Basic type      |   Example  |
|----------|------------------------|------------|
| `int`    | Integer numbers        | `42`       |
| `float`  | Floating point numbers | `3.14`     |
| `str`    | Strings and characters | `"cheese"` |
| `bool `  | Boolean values         | `True`     |

It's possible to determine the type of a Python variable using the built-in `type` function. For example,
```python
>>> x = 5
>>> type(x)
<class 'int'>
```

**Task 3:** Use interactive mode to determine the type of each variable below using the `type` function.
```python
a = 9001
b = "3"
c = False
d = 2.718281828
e = "apple"
```

## Getting user input
We can use the `input` function to make our scripts interactive. 

**Task 4:** Save the following code as `fav_fruit.py` then try running it.
```python
fav_fruit = input("What is your favourite fruit? ")

print("The user's favourite fruit is:", fav_fruit)
```

**Task 5:** Write a script that asks the user to enter the height and base of a triangle, then calculates the area.

**Task 6:** Write a script that calculates the surface areas of octohedrons with side lengths of 1 cm, 2 cm, 3 cm and 4 cm.

## Functions
Task 6 motivates the use of functions: sometimes you need to re-use code. A convenient way to do this is to define a function. For example:
```python
import math

def sphere_surface_area(radius):
    area = 4 * math.pi * radius**2
    return area

r = 1
s = sphere_surface_area(r)
print(f"The surface area of a sphere of radius {r} cm is {s} cm^2")

R = 4
S = sphere_surface_area(R)
print(f"The surface area of a sphere of radius {R} cm is {S} cm^2")
```

**Task 7:** define a function that calculates the surface area of an octohedron. Calculate the surface area of octohedra with side lengths of 1 cm, 2 cm, 3 cm and 4 cm. You should obtain the same answers as in Task 6.

## Loops
In Task 7, you needed to call the function many times. A nice way to do this is with loops:
```python
radii = [1, 2, 3, 4, 5, 6, 7, 8]
for radius in radii:
    surface_area = sphere_surface_area(radius)
    print(f"The surface area of a sphere of radius {radius} cm is {surface_area} cm^2")
```

**Task 8:** replace the repeat function calls in your answer to Task 7 with a loop, similar to the above example.