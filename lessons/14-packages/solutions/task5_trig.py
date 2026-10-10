import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)

plt.plot(x, np.sin(x), label=r"$y = \sin x$")
plt.plot(x, np.cos(x), label=r"$y = \cos x$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Sine and cosine")
plt.legend()
plt.grid()
plt.savefig("trig.png")
plt.show()

# The `r` before the strings above makes them "raw" strings, where backslashes
# are just backslashes. Without it, Python might treat `\s` or `\c` as escape
# characters (like `\n`), and complain.
