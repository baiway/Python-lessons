class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        """Adds `data` to the front of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        """Adds `data` to the end of the list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def __str__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return " -> ".join(items)

    def delete(self, data):
        """Removes the first node containing `data`"""
        if self.head is None:
            raise ValueError(f"{data} is not in the list")

        # Special case: deleting the head
        if self.head.data == data:
            self.head = self.head.next
            return

        # Otherwise, find the node BEFORE the one we want to delete
        previous = self.head
        while previous.next is not None and previous.next.data != data:
            previous = previous.next
        if previous.next is None:
            raise ValueError(f"{data} is not in the list")

        # Skip over the deleted node
        previous.next = previous.next.next


numbers = LinkedList()
for n in [3, 8, 5, 2]:
    numbers.append(n)
print(numbers)      # 3 -> 8 -> 5 -> 2

numbers.delete(3)   # the head
print(numbers)      # 8 -> 5 -> 2
numbers.delete(5)   # the middle
print(numbers)      # 8 -> 2
numbers.delete(2)   # the end
print(numbers)      # 8

try:
    numbers.delete(42)
except ValueError as error:
    print(f"Error: {error}")
