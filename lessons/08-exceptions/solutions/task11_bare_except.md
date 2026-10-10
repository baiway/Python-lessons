# Task 9 solution
Pressing `Ctrl` + `c` doesn't stop the program! Instead, it prints "Something went wrong! Try again." and asks for another number.

This happens because pressing `Ctrl` + `c` works by raising an exception called `KeyboardInterrupt`. Normally, this crashes the program (which is what we want). But a bare `except:` catches _every_ exception, including `KeyboardInterrupt`, so our program catches it, prints its message, and carries on. The only way to stop it is to close the terminal (in VS Code, click the bin icon in the terminal panel).

The fix is to only catch the exception we're actually expecting:
```python
while True:
    try:
        number = int(input("Enter a whole number: "))
        print(f"{number} squared is {number**2}")
    except ValueError:
        print("That's not a whole number! Try again.")
```

This is a good example of why bare `except:` statements are dangerous: they hide problems that you weren't expecting, which makes bugs very hard to track down.
