# Try to stop this program by pressing Ctrl + c. What happens?
while True:
    try:
        number = int(input("Enter a whole number: "))
        print(f"{number} squared is {number**2}")
    except:
        print("Something went wrong! Try again.")
