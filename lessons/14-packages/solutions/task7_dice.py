import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
num_rolls = 10_000

# Roll two dice 10,000 times each, and add them together
totals = rng.integers(1, 7, size=num_rolls) + rng.integers(1, 7, size=num_rolls)

# Count how many times each total from 2 to 12 came up
possible_totals = np.arange(2, 13)
counts = [(totals == total).sum() for total in possible_totals]

plt.bar(possible_totals, counts)
plt.xticks(possible_totals)
plt.xlabel("Total")
plt.ylabel("Number of rolls")
plt.title(f"Rolling two dice {num_rolls:,} times")
plt.savefig("dice.png")
plt.show()
