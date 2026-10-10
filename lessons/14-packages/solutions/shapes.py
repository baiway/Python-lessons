import math

def sphere_surface_area(radius):
    """Calculates the surface area of a sphere with the given radius"""
    return 4 * math.pi * radius**2


def octahedron_surface_area(side_length):
    """Calculates the surface area of an octahedron with the given side length"""
    return 2 * side_length**2 * math.sqrt(3)


if __name__ == "__main__":
    # Quick checks, which only run if you run `python shapes.py`
    print(sphere_surface_area(1))      # 12.566...
    print(octahedron_surface_area(1))  # 3.464...
