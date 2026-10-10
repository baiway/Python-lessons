class CircularQueue:
    def __init__(self, capacity):
        self._items = [None] * capacity
        self._capacity = capacity
        self._front = 0  # index of the next item to dequeue
        self._rear = 0   # index where the next item will be enqueued
        self._size = 0   # number of items currently in the queue

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("The queue is full")
        self._items[self._rear] = item
        self._rear = (self._rear + 1) % self._capacity  # wrap around to 0
        self._size = self._size + 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty")
        item = self._items[self._front]
        self._items[self._front] = None  # not necessary, but makes printing clearer
        self._front = (self._front + 1) % self._capacity
        self._size = self._size - 1
        return item

    def __str__(self):
        return f"{self._items} (front={self._front}, rear={self._rear})"


queue = CircularQueue(4)
for letter in "ABCD":
    queue.enqueue(letter)
print(queue)

try:
    queue.enqueue("E")
except OverflowError as error:
    print(f"Error: {error}")

print(f"Dequeued {queue.dequeue()}")
print(f"Dequeued {queue.dequeue()}")
print(queue)

# The rear index wraps around to the start of the list
queue.enqueue("E")
queue.enqueue("F")
print(queue)

while not queue.is_empty():
    print(f"Dequeued {queue.dequeue()}")
