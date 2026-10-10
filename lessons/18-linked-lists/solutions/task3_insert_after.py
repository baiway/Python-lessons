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

    def insert_after(self, target, data):
        """Inserts `data` immediately after the first node containing `target`"""
        current = self.head
        while current is not None and current.data != target:
            current = current.next
        if current is None:
            raise ValueError(f"{target} is not in the list")

        # Point the new node at the next node FIRST, then point the current
        # node at the new node
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node


numbers = LinkedList()
for n in [3, 8, 5]:
    numbers.append(n)

numbers.insert_after(8, 7)
print(numbers)  # 3 -> 8 -> 7 -> 5
numbers.insert_after(5, 9)
print(numbers)  # 3 -> 8 -> 7 -> 5 -> 9

try:
    numbers.insert_after(42, 1)
except ValueError as error:
    print(f"Error: {error}")
