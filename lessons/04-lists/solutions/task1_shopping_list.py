shopping = ["eggs", "milk", "bread"]

print(f"First item: {shopping[0]}")
print(f"Last item: {shopping[-1]}")

shopping.append("cheese")
shopping.remove("milk")

print(shopping)
print(f"There are {len(shopping)} items on the list")
