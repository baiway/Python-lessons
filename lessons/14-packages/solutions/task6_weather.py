import matplotlib.pyplot as plt
import numpy as np

# Load the temperatures (columns 1 and 2) and the dates (column 0) separately,
# because numpy arrays usually contain just one type of data
temperatures = np.loadtxt("weather.csv", delimiter=",", skiprows=1, usecols=(1, 2))
dates = np.loadtxt("weather.csv", delimiter=",", skiprows=1, usecols=0, dtype=str)

max_temps = temperatures[:, 0]
min_temps = temperatures[:, 1]

plt.plot(dates, max_temps, marker="o", label="Maximum")
plt.plot(dates, min_temps, marker="o", label="Minimum")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Daily temperatures")
plt.xticks(rotation=45, ha="right")  # rotate the dates so they don't overlap
plt.legend()
plt.grid()
plt.tight_layout()  # make sure the rotated dates fit in the image
plt.savefig("weather.png")
plt.show()
