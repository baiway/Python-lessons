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


stack = Stack()
for item in ["first", "second", "third"]:
    stack.push(item)
    print(f"Pushed {item}")

print(f"The top item is {stack.peek()}, and there are {len(stack)} items")

while not stack.is_empty():
    print(f"Popped {stack.pop()}")

try:
    stack.pop()
except IndexError as error:
    print(f"Error: {error}")
