class ArrayLinkedList:
    """A linked list stored in two fixed-size arrays, with a free list"""

    def __init__(self, capacity):
        self.data = [None] * capacity
        self.next = [-1] * capacity
        self.head = -1  # -1 means "no node"

        # At the start, every space is free, and each one points to the next
        for i in range(capacity - 1):
            self.next[i] = i + 1
        self.free = 0 if capacity > 0 else -1

    def append(self, item):
        """Adds `item` to the end of the list"""
        if self.free == -1:
            raise OverflowError("The list is full")

        # Take the first space from the free list
        new = self.free
        self.free = self.next[new]
        self.data[new] = item
        self.next[new] = -1

        if self.head == -1:
            self.head = new
        else:
            current = self.head
            while self.next[current] != -1:
                current = self.next[current]
            self.next[current] = new

    def delete(self, item):
        """Removes the first node containing `item`, and frees its space"""
        previous = -1
        current = self.head
        while current != -1 and self.data[current] != item:
            previous = current
            current = self.next[current]
        if current == -1:
            raise ValueError(f"{item} is not in the list")

        # Skip over the deleted node...
        if previous == -1:
            self.head = self.next[current]
        else:
            self.next[previous] = self.next[current]

        # ...and add its space to the front of the free list
        self.data[current] = None
        self.next[current] = self.free
        self.free = current

    def to_list(self):
        """Returns the items as a Python list, in order"""
        items = []
        current = self.head
        while current != -1:
            items.append(self.data[current])
            current = self.next[current]
        return items


numbers = ArrayLinkedList(5)
for n in [3, 8, 5]:
    numbers.append(n)
print(numbers.to_list())                 # [3, 8, 5]
print(numbers.data, numbers.next, numbers.head, numbers.free)

numbers.delete(3)
print(numbers.to_list())                 # [8, 5]
print(numbers.data, numbers.next, numbers.head, numbers.free)

# The freed space (index 0) is reused for the next item
numbers.append(7)
print(numbers.to_list())                 # [8, 5, 7]
print(numbers.data, numbers.next, numbers.head, numbers.free)

numbers.append(1)
numbers.append(2)
try:
    numbers.append(9)
except OverflowError as error:
    print(f"Error: {error}")
