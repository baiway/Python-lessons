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

    def reverse(self):
        """Reverses the list in place, by changing the pointers"""
        previous = None
        current = self.head
        while current is not None:
            following = current.next  # remember the rest of the list...
            current.next = previous   # ...before turning this pointer round
            previous = current
            current = following
        self.head = previous  # the old last node is the new head


numbers = LinkedList()
for n in [1, 2, 3, 4, 5]:
    numbers.append(n)
print(numbers)  # 1 -> 2 -> 3 -> 4 -> 5
numbers.reverse()
print(numbers)  # 5 -> 4 -> 3 -> 2 -> 1

empty = LinkedList()
empty.reverse()  # should do nothing (and not crash!)
print(f"[{empty}]")
