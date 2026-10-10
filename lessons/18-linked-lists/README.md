# Lesson 18: Linked lists
In [Lesson 16](../16-recursion-stacks-and-queues), we met two _abstract data types_ (ADTs): stacks and queues. An ADT describes _what_ a data structure does (the operations you can perform on it, like push and pop), without saying _how_ it does it. In this lesson and the next two, we'll look at some more ADTs, and build them ourselves from scratch. These lessons go beyond what's needed for GCSE, but they're part of IB Computer Science (HL) and A Level Computer Science.

We'll start with the _linked list_. Like a Python list, a linked list stores a sequence of items in order. But it stores them in a completely different way, which makes some operations much faster, and others much slower.

## Nodes and pointers
In a linked list, each item is stored in its own little object, called a _node_. As well as the item itself (its _data_), each node stores a _pointer_ (or _reference_) to the next node in the list. The list itself only needs to remember where the first node is, which is called the _head_. The last node's pointer is `None`, to show that there's nothing after it.
```
 head
  │
  ▼
┌───┬───┐    ┌───┬───┐    ┌───┬──────┐
│ 3 │ ●─┼───►│ 8 │ ●─┼───►│ 5 │ None │
└───┴───┘    └───┴───┘    └───┴──────┘
```

In Python, a node is a very simple class:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # the next node in the list (None if there isn't one)
```

We can then link some nodes together by hand, and _traverse_ the list (visit each node in turn) by following the pointers until we reach `None`:
```python
head = Node(3)
head.next = Node(8)
head.next.next = Node(5)

current = head
while current is not None:
    print(current.data)
    current = current.next  # follow the pointer to the next node
```

(`is not None` is the usual way of checking whether something isn't `None` in Python. It works just like `!= None`.)

**Task 1:** Create a linked list containing the days of the week, by creating seven `Node` objects and linking them together. Then traverse the list, printing each day. Finally, count the number of nodes in the list by traversing it again. [Solution](solutions/task1_days_of_the_week.py)

## A linked list class
Linking nodes together by hand quickly gets fiddly, so let's wrap the linked list up in a class with some useful methods. To add an item to the _front_ of the list, we create a new node, point it at the current head, and make it the new head. To add an item to the _end_ of the list, we have to traverse the whole list to find the last node, then point the last node at the new node.
```python
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
```

You can find this class in [`examples/linked_list.py`](examples/linked_list.py).

**Task 2:** Add a `__len__` method to the `LinkedList` class above, which returns the number of items in the list, and a `search(data)` method, which returns `True` if `data` is in the list and `False` otherwise. Test both on a few lists, including an empty one. [Solution](solutions/task2_len_and_search.py)

## Inserting and deleting
The big advantage of a linked list is that inserting or deleting an item in the middle of the list doesn't require moving any other items: we just change a couple of pointers. To insert a new node after an existing node, first point the new node at the node that comes after it, then point the existing node at the new node. (If you do these the other way round, you lose track of the rest of the list!) For example, to insert 7 after 8:
```
Before:                    3 ──► 8 ──► 5 ──► None
1. Point 7 at 5:                       7 ──► 5
2. Point 8 at 7:           3 ──► 8 ──► 7 ──► 5 ──► None
```

To delete a node, find the node _before_ it, and point it at the node _after_ it. The deleted node is skipped over, and Python's _garbage collector_ automatically frees up its memory once nothing points to it any more. Be careful with the special case of deleting the head node, which doesn't have a node before it: in that case, the second node becomes the new head.

Compare this with a Python list (or an array): to insert an item in the middle, every item after it has to shuffle one place to the right to make room. The table below compares the two (see [Lesson 10](../10-searching-and-sorting) for a reminder of Big O notation).

| Operation                                   | Python list (array)  | Linked list                                     |
|---------------------------------------------|----------------------|-------------------------------------------------|
| Get the item at index `i`                   | $O(1)$               | $O(n)$: you have to follow `i` pointers          |
| Add an item at the front                    | $O(n)$               | $O(1)$                                          |
| Add an item at the end                      | $O(1)$ (usually)     | $O(n)$, or $O(1)$ if you also keep a `tail` pointer |
| Insert or delete after a node you've found  | $O(n)$               | $O(1)$                                          |
| Search for an item                          | $O(n)$               | $O(n)$                                          |
| Memory used                                 | Just the items       | The items, plus a pointer for each item         |

**Task 3:** Add an `insert_after(target, data)` method to your `LinkedList` class, which inserts `data` immediately after the first node containing `target`. It should raise a `ValueError` if `target` isn't in the list. [Solution](solutions/task3_insert_after.py)

**Task 4:** Add a `delete(data)` method, which removes the first node containing `data`. Make sure it works when `data` is at the start, in the middle, or at the end of the list, and raises a `ValueError` if `data` isn't in the list. [Solution](solutions/task4_delete.py)

**Task 5:** Draw diagrams (like the ones above) showing the state of a linked list after each of the operations below, starting from an empty list. Then check your answer by running the operations on your class. [Solution](solutions/task5_diagrams.md)
1. `append(4)`
2. `append(9)`
3. `prepend(1)`
4. `insert_after(1, 6)`
5. `delete(9)`
6. `delete(1)`

## Doubly linked lists
In a _doubly linked list_, each node has two pointers: `next`, which points to the next node, and `prev`, which points to the previous node. The list usually keeps track of its last node (the _tail_) as well as its head. This uses more memory, but it means that you can traverse the list in either direction, add items to either end in $O(1)$ time, and delete a node without having to search for the node before it.
```
head ──► [None | 3 | ●] ◄──► [● | 8 | ●] ◄──► [● | 5 | None] ◄── tail
```

Here, each node is drawn as `[prev | data | next]`.

The disadvantage is that every operation has to keep both sets of pointers correct, which makes the code trickier to get right.

**Task 6:** Write a `DoublyLinkedList` class (with a `DoublyNode` class whose nodes have `data`, `next` and `prev` attributes). Give it `append`, `prepend` and `delete(data)` methods, and two methods that return the items as a Python list: one going forwards from the head, and one going backwards from the tail. Use them to check that your `next` and `prev` pointers always agree. [Solution](solutions/task6_doubly_linked_list.py)

## Circular linked lists
In a _circular linked list_, the last node points back to the first node, instead of to `None`. There's no natural start or end, which makes them a good fit for things that go round and round: for example, taking turns in a game, or a music playlist on repeat. Be careful when traversing a circular linked list: there's no `None` to stop at, so you have to stop when you get back to where you started!

**Task 7:** Use a circular linked list to simulate a game of "pass the parcel". The players sit in a circle, and the parcel starts with the first player and is passed from player to player. Each time the music stops (after every `k` passes), the player holding the parcel is out, and is removed from the circle. The game continues until one player is left. Write a function `pass_the_parcel(players, k)` that returns the winner, printing who is out at each stage. Who wins with players `["Ada", "Alan", "Grace", "Tim", "Linus"]` and `k = 3`? [Solution](solutions/task7_pass_the_parcel.py)

## Linked lists in arrays
In some languages (and in many exam questions!), linked lists are stored using arrays rather than objects. One array stores the data, and a second array stores the pointers, which are just indexes into the arrays. A variable stores the index of the head, and a special value (often `-1`) is used instead of `None`. Free spaces in the arrays are kept in a second linked list (the _free list_), so that the program knows where to put new items.

For example, the list `3 -> 8 -> 5` might be stored like this, with `head = 2` and `free = 1`:

| Index | `data` | `next` |
|-------|--------|--------|
| 0     | 8      | 3      |
| 1     |        | 4      |
| 2     | 3      | 0      |
| 3     | 5      | -1     |
| 4     |        | -1     |

Follow the pointers from `head`: index 2 holds 3 and points to index 0, which holds 8 and points to index 3, which holds 5 and points to -1 (the end). The free list starts at index 1, which points to index 4, which is the last free space.

**⭐ Task 8:** Write an `ArrayLinkedList` class that stores a linked list of up to `capacity` items in two fixed-size Python lists (`data` and `next`), with a free list as described above. Give it `append`, `delete(data)` and `to_list` methods. When you delete an item, its space should be added back to the free list, so that it can be reused. [Solution](solutions/task8_array_linked_list.py)

**⭐ Task 9:** Add a `reverse()` method to your singly linked `LinkedList` class, which reverses the list _in place_ (i.e. by changing the pointers, without creating any new nodes). Hint: you'll need to keep track of three nodes as you go: the previous node, the current node, and the next node. Draw some diagrams first! [Solution](solutions/task9_reverse.py)

---
[← Previous: Lesson 17](../17-testing) | [Contents](../../README.md) | [Next: Lesson 19 →](../19-binary-search-trees)
