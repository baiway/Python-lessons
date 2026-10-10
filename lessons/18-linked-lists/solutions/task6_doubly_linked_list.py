class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Adds `data` to the end of the list"""
        new_node = DoublyNode(data)
        if self.tail is None:  # the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """Adds `data` to the front of the list"""
        new_node = DoublyNode(data)
        if self.head is None:  # the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        """Removes the first node containing `data`"""
        current = self.head
        while current is not None and current.data != data:
            current = current.next
        if current is None:
            raise ValueError(f"{data} is not in the list")

        # Point the nodes either side of `current` at each other. If there
        # isn't a node on one side, then `current` was the head or the tail.
        if current.prev is None:
            self.head = current.next
        else:
            current.prev.next = current.next

        if current.next is None:
            self.tail = current.prev
        else:
            current.next.prev = current.prev

    def forwards(self):
        """Returns the items as a Python list, from head to tail"""
        items = []
        current = self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items

    def backwards(self):
        """Returns the items as a Python list, from tail to head"""
        items = []
        current = self.tail
        while current is not None:
            items.append(current.data)
            current = current.prev
        return items


letters = DoublyLinkedList()
for letter in "BCD":
    letters.append(letter)
letters.prepend("A")
print(letters.forwards())   # ['A', 'B', 'C', 'D']
print(letters.backwards())  # ['D', 'C', 'B', 'A']

for letter in ["A", "C", "D"]:  # the head, the middle and the tail
    letters.delete(letter)
    print(letters.forwards(), letters.backwards())

# If the `next` and `prev` pointers agree, going backwards gives the same
# items as going forwards, in reverse
print(letters.forwards() == letters.backwards()[::-1])  # True
