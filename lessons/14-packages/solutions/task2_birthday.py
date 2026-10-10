import datetime

month = int(input("What month is your birthday (1-12)? "))
day = int(input("What day of the month is your birthday? "))

today = datetime.date.today()
next_birthday = datetime.date(today.year, month, day)

# If this year's birthday has already been, the next one is next year
if next_birthday < today:
    next_birthday = datetime.date(today.year + 1, month, day)

days_left = (next_birthday - today).days
if days_left == 0:
    print("Happy birthday!")
else:
    print(f"There are {days_left} days until your next birthday.")
