def mean_of_valid(entries):
    """Returns the mean of the entries that can be converted to a float, and
    the number of entries that were skipped"""
    valid = []
    num_skipped = 0
    for entry in entries:
        try:
            valid.append(float(entry))
        except ValueError:
            num_skipped = num_skipped + 1

    # If there are no valid entries, there's no sensible mean to return, so we
    # raise an exception rather than dividing by zero
    if len(valid) == 0:
        raise ValueError("None of the entries are valid numbers")

    return sum(valid) / len(valid), num_skipped


entries = ["12", "7.5", "banana", "3", "", "-4", "1O", "8.25"]
mean, num_skipped = mean_of_valid(entries)
print(f"Mean of valid entries: {mean:.2f} ({num_skipped} entries skipped)")

try:
    mean_of_valid(["one", "two", "three"])
except ValueError as error:
    print(f"Error: {error}")
