try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("That's not a whole number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"100 / {number} = {result}")
finally:
    print("Thanks for using my program!")
