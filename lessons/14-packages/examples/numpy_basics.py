import numpy as np

# Doing maths on whole arrays at once
heights = np.array([1.62, 1.75, 1.58, 1.81])  # in metres
heights_cm = heights * 100
print(heights_cm)
print(heights.mean(), heights.max())

# Compare with a normal list!
print([1, 2, 3] * 2)

# Other useful features
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))
print(np.sqrt(heights))
print(heights > 1.7)
print(heights[heights > 1.7])
print((heights > 1.7).sum())

# 2D arrays
grid = np.array([[1, 2, 3], [4, 5, 6]])
print(grid.shape)
print(grid[1, 2])
print(grid[:, 1])
print(grid.sum(axis=0))
