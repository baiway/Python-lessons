temperatures = [18.2, 21.5, 19.8, 23.1, 25.4, 22.0, 17.6]

# Start `highest` and `lowest` at the first temperature, then update them
# whenever we find something higher or lower
total = 0
highest = temperatures[0]
lowest = temperatures[0]
for temp in temperatures:
    total = total + temp
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

mean = total / len(temperatures)

print(f"Total: {total:.1f} °C")
print(f"Mean: {mean:.1f} °C")
print(f"Highest: {highest} °C")
print(f"Lowest: {lowest} °C")

# Check using the built-in functions
print(f"Check: {sum(temperatures):.1f}, {max(temperatures)}, {min(temperatures)}")
