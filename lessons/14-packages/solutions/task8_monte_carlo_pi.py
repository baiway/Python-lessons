import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
num_darts = 10_000

# Throw darts at random points in the square from (-1, -1) to (1, 1)
x = rng.uniform(-1, 1, size=num_darts)
y = rng.uniform(-1, 1, size=num_darts)

# A dart is inside the circle if its distance from the centre is at most 1
inside = x**2 + y**2 <= 1
pi_estimate = 4 * inside.sum() / num_darts
print(f"Estimate of pi: {pi_estimate}")

# `~inside` flips every True to False and vice versa
plt.scatter(x[inside], y[inside], s=1, label="Inside")
plt.scatter(x[~inside], y[~inside], s=1, label="Outside")
plt.gca().set_aspect("equal")  # make sure the circle looks like a circle
plt.title(rf"$\pi \approx {pi_estimate}$")
# Put the legend below the plot (so it doesn't cover any darts), with bigger dots
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=2, markerscale=8)
plt.tight_layout()
plt.savefig("monte_carlo_pi.png")
plt.show()
