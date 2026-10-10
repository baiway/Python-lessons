phone_book = {}

while True:
    print()
    print("1. Add a number")
    print("2. Look up a number")
    print("3. Delete a number")
    print("4. List everyone")
    print("5. Quit")
    choice = input("What would you like to do? ")

    if choice == "1":
        name = input("Name: ")
        number = input("Phone number: ")
        phone_book[name] = number
        print(f"Added {name}")
    elif choice == "2":
        name = input("Name: ")
        print(phone_book.get(name, f"Sorry, {name} isn't in the phone book"))
    elif choice == "3":
        name = input("Name: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Deleted {name}")
        else:
            print(f"Sorry, {name} isn't in the phone book")
    elif choice == "4":
        for name in sorted(phone_book):
            print(f"{name}: {phone_book[name]}")
    elif choice == "5":
        break
    else:
        print("Please choose a number from 1 to 5")
