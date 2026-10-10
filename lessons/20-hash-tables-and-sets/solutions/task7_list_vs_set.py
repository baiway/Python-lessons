import time

numbers_list = list(range(100_000))
numbers_set = set(numbers_list)

start = time.perf_counter()
for n in range(99_000, 100_000):
    n in numbers_list
list_time = time.perf_counter() - start

start = time.perf_counter()
for n in range(99_000, 100_000):
    n in numbers_set
set_time = time.perf_counter() - start

print(f"List: {list_time:.5f} seconds")
print(f"Set:  {set_time:.5f} seconds")
print(f"The set was about {list_time / set_time:.0f} times faster")

# Checking whether an item is in a list is a linear search, which takes O(n)
# time (and these numbers are all near the end of the list). A set is a hash table, so it just calculates the item's hash and looks
# in one slot, which takes O(1) time on average, however big the set is.
