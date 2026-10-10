names = ["Ada", "Alan", "Grace", "Tim", "Margaret", "Linus", "Guido"]
target = input("Enter a name to search for: ")

# Check each item in turn, stopping as soon as we find a match
found = False
for i, name in enumerate(names):
    if name == target:
        print(f"Found {target} at index {i}")
        found = True
        break

if not found:
    print(f"{target} is not in the list")
