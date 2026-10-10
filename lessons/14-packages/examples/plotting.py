import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)

plt.plot(x, x**2, label="$y = x^2$")
plt.plot(x, x**3, label="$y = x^3$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Some polynomials")
plt.legend()
plt.grid()
plt.savefig("polynomials.png")  # saves the graph as an image
plt.show()                      # opens a window showing the graph
