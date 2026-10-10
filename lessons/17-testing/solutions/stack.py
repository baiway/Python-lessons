class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        """Adds `item` to the top of the stack"""
        self._items.append(item)

    def pop(self):
        """Removes the item from the top of the stack, and returns it"""
        if self.is_empty():
            raise IndexError("Can't pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """Returns the item on the top of the stack, without removing it"""
        if self.is_empty():
            raise IndexError("Can't peek at an empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)
