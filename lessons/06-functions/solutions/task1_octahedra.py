import math

def octahedron_surface_area(side_length):
    """Calculates the surface area of an octahedron with the given side length"""
    return 2 * side_length**2 * math.sqrt(3)

# Define side lengths of interest in a list
side_lengths = [1, 2, 3, 4]

# Loop over side lengths
for a in side_lengths:
    print(f"The surface area of an octahedron with side length {a} cm is {octahedron_surface_area(a):.2f} cm^2.")
