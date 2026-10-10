import shapes

print(f"{'Size (cm)':>10} {'Sphere (cm^2)':>15} {'Octahedron (cm^2)':>19}")
for size in range(1, 6):
    sphere = shapes.sphere_surface_area(size)
    octahedron = shapes.octahedron_surface_area(size)
    print(f"{size:>10} {sphere:>15.2f} {octahedron:>19.2f}")
