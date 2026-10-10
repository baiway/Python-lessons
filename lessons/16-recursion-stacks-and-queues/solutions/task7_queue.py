from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Adds `item` to the back of the queue"""
        self._items.append(item)

    def dequeue(self):
        """Removes the item from the front of the queue, and returns it"""
        if self.is_empty():
            raise IndexError("Can't dequeue from an empty queue")
        return self._items.popleft()

    def peek(self):
        """Returns the item at the front of the queue, without removing it"""
        if self.is_empty():
            raise IndexError("Can't peek at an empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


printer_queue = Queue()
for document in ["essay.docx", "homework.pdf", "photo.jpg", "slides.pptx", "notes.txt"]:
    printer_queue.enqueue(document)
    print(f"Added {document} to the queue")

print(f"Next up: {printer_queue.peek()}")

while not printer_queue.is_empty():
    document = printer_queue.dequeue()
    print(f"Printing {document}... {len(printer_queue)} documents still waiting")
