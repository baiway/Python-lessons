try:
    a = float(input("Enter a number: "))
    b = float(input("Enter a number to divide it by: "))
    print(f"{a} / {b} = {a / b}")
except ValueError:
    print("Please only enter numbers.")
except ZeroDivisionError:
    print("You can't divide by zero!")
