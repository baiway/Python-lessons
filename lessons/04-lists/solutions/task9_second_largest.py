numbers = [12, 45, 7, 45, 23, 38, 9]

# Keep track of the largest and second largest numbers seen so far. `None` is
# Python's way of saying "no value": we don't have a second largest number yet!
largest = numbers[0]
second_largest = None
for number in numbers[1:]:
    if number > largest:
        second_largest = largest
        largest = number
    elif number < largest and (second_largest is None or number > second_largest):
        second_largest = number

print(f"The largest number is {largest}")
print(f"The second largest number is {second_largest}")
