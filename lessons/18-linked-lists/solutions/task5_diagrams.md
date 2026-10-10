# Task 5 solution
Starting from an empty list (`head ──► None`):

1. `append(4)`: the list was empty, so the new node becomes the head.
   ```
   head ──► [4 | ●] ──► None
   ```
2. `append(9)`: traverse to the last node (4), and point it at the new node.
   ```
   head ──► [4 | ●] ──► [9 | ●] ──► None
   ```
3. `prepend(1)`: point the new node at the old head (4), then make it the new head.
   ```
   head ──► [1 | ●] ──► [4 | ●] ──► [9 | ●] ──► None
   ```
4. `insert_after(1, 6)`: point the new node at 1's next node (4), then point 1 at the new node.
   ```
   head ──► [1 | ●] ──► [6 | ●] ──► [4 | ●] ──► [9 | ●] ──► None
   ```
5. `delete(9)`: find the node before 9 (that's 4), and point it at the node after 9 (`None`).
   ```
   head ──► [1 | ●] ──► [6 | ●] ──► [4 | ●] ──► None
   ```
6. `delete(1)`: 1 is the head, so the second node (6) becomes the new head.
   ```
   head ──► [6 | ●] ──► [4 | ●] ──► None
   ```

You can check this with your class:
```python
numbers = LinkedList()
numbers.append(4)
numbers.append(9)
numbers.prepend(1)
numbers.insert_after(1, 6)
numbers.delete(9)
numbers.delete(1)
print(numbers)  # 6 -> 4
```
