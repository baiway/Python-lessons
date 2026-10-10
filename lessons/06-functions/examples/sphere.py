import math

def sphere_surface_area(radius):
    """Calculates the surface area of a sphere with the given radius"""
    area = 4 * math.pi * radius**2
    return area

# Call the function a few times with different inputs
r = 1
s = sphere_surface_area(r)
print(f"The surface area of a sphere of radius {r} cm is {s:.2f} cm^2")

R = 4
S = sphere_surface_area(R)
print(f"The surface area of a sphere of radius {R} cm is {S:.2f} cm^2")

# Or, even better, use a loop
radii = [1, 2, 3, 4, 5, 6, 7, 8]
for radius in radii:
    surface_area = sphere_surface_area(radius)
    print(f"The surface area of a sphere of radius {radius} cm is {surface_area:.2f} cm^2")
