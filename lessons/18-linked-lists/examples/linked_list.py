class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # the next node in the list (None if there isn't one)


class LinkedList:
    def __init__(self):
        self.head = None  # an empty list has no nodes

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


# Linking nodes together by hand, then traversing them
head = Node(3)
head.next = Node(8)
head.next.next = Node(5)

current = head
while current is not None:
    print(current.data)
    current = current.next

# Using the LinkedList class
numbers = LinkedList()
numbers.append(8)
numbers.append(5)
numbers.prepend(3)
print(numbers)  # 3 -> 8 -> 5
