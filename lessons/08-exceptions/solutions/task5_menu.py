menu = ["Pizza", "Burger", "Pasta", "Salad", "Soup"]

# Print the menu, numbered from 1
for i, item in enumerate(menu):
    print(f"{i + 1}. {item}")

try:
    choice = int(input("Choose an item: "))

    # Negative numbers don't cause an IndexError (e.g. menu[-1] is the last
    # item), and nor does 0 (menu[0 - 1] is menu[-1]!), so we need to check
    # for these ourselves
    if choice < 1:
        print(f"Please enter a number between 1 and {len(menu)}.")
    else:
        print(f"You chose: {menu[choice - 1]}")
except ValueError:
    print("Please enter a number.")
except IndexError:
    print(f"Please enter a number between 1 and {len(menu)}.")
