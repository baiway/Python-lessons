import numpy as np

temperatures = np.array([18.2, 21.5, 19.8, 23.1, 25.4, 22.0, 17.6])

# 1. Mean, highest and lowest
print(f"Mean: {temperatures.mean():.1f} °C")
print(f"Highest: {temperatures.max()} °C")
print(f"Lowest: {temperatures.min()} °C")

# 2. Convert to Fahrenheit (this converts every temperature at once!)
fahrenheit = 9/5 * temperatures + 32
print(f"In Fahrenheit: {fahrenheit}")

# 3. Count the days warmer than 20 °C
print(f"Days warmer than 20 °C: {(temperatures > 20).sum()}")

# 4. Temperatures above the mean
print(f"Above the mean: {temperatures[temperatures > temperatures.mean()]}")
