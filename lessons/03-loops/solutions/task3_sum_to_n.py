n = int(input("Enter a whole number: "))

# Add up the numbers from 1 to n
total = 0
for i in range(1, n + 1):
    total = total + i

print(f"The sum of the numbers from 1 to {n} is {total}")
print(f"Using the formula n(n+1)/2: {n * (n + 1) // 2}")
