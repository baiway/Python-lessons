class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Can't pop from an empty stack")
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0


# Each closing bracket, and the opening bracket it should match
MATCHING = {")": "(", "]": "[", "}": "{"}


def is_balanced(text):
    """Returns `True` if the brackets in `text` are balanced"""
    stack = Stack()
    for char in text:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            # A closing bracket with nothing to match it
            if stack.is_empty():
                return False
            if stack.pop() != MATCHING[char]:
                return False

    # Any brackets left on the stack were never closed
    return stack.is_empty()


for text in ["(a[b]{c})", "(a[b)]", "((a)", "a)", "print(f'{x[0]}')", ""]:
    print(f"{text!r}: {is_balanced(text)}")
