import geometry

# Importing `geometry` doesn't run its test code, because `__name__` isn't
# "__main__" when a file is imported
for radius in [1, 2, 3]:
    print(f"A circle of radius {radius} has area {geometry.circle_area(radius):.2f}")
