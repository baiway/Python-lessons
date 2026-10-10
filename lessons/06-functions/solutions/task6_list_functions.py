def mean(numbers):
    """Returns the mean of a list of numbers"""
    return sum(numbers) / len(numbers)


def linear_search(items, target):
    """Returns the index of `target` in `items`, or -1 if it isn't there"""
    for i in range(len(items)):
        if items[i] == target:
            return i  # this exits the function (and so the loop) straight away
    return -1


def count_above(numbers, threshold):
    """Returns how many numbers in the list are greater than `threshold`"""
    count = 0
    for number in numbers:
        if number > threshold:
            count = count + 1
    return count


scores = [72, 85, 64, 90, 58]
names = ["Ada", "Alan", "Grace", "Tim"]

print(mean(scores))                 # 73.8
print(mean([1, 2, 3, 4]))           # 2.5
print(linear_search(names, "Grace"))  # 2
print(linear_search(names, "Bob"))    # -1
print(count_above(scores, 70))      # 3
print(count_above(scores, 100))     # 0
