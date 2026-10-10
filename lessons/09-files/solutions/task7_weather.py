dates = []
max_temps = []
min_temps = []

with open("weather.csv", encoding="utf-8") as file:
    next(file)  # skip the header
    for line in file:
        values = line.strip().split(",")
        dates.append(values[0])
        max_temps.append(float(values[1]))
        min_temps.append(float(values[2]))

# Find the hottest day and the coldest night
hottest = 0
coldest = 0
for i in range(len(dates)):
    if max_temps[i] > max_temps[hottest]:
        hottest = i
    if min_temps[i] < min_temps[coldest]:
        coldest = i

mean_max = sum(max_temps) / len(max_temps)

# Write the summary to a file, then print it too
summary = (
    f"Weather summary for {dates[0]} to {dates[-1]}\n"
    f"Hottest day: {dates[hottest]} ({max_temps[hottest]} °C)\n"
    f"Coldest night: {dates[coldest]} ({min_temps[coldest]} °C)\n"
    f"Mean maximum temperature: {mean_max:.1f} °C\n"
)

with open("weather_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print(summary)
