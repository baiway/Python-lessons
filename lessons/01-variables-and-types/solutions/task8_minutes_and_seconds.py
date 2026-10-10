total_seconds = int(input("Enter a number of seconds: "))

minutes = total_seconds // 60  # number of whole minutes
seconds = total_seconds % 60   # seconds left over

print(f"{total_seconds} seconds is {minutes} minutes and {seconds} seconds")
