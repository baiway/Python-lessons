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

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.next
        return count

    def search(self, data):
        """Returns `True` if `data` is in the list"""
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False


numbers = LinkedList()
print(len(numbers), numbers.search(3))  # 0 False

for n in [3, 8, 5]:
    numbers.append(n)
print(numbers)                          # 3 -> 8 -> 5
print(len(numbers))                     # 3
print(numbers.search(8))                # True
print(numbers.search(4))                # False
