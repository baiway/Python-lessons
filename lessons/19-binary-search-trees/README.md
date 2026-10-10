# Lesson 19: Binary search trees
In [Lesson 18](../18-linked-lists), each node pointed to (at most) one other node, making a chain. In this lesson, we'll let each node point to _two_ other nodes, making a _tree_. In particular, we'll look at _binary search trees_, which store items in a way that makes searching for them very fast, a bit like [binary search](../10-searching-and-sorting).

## Trees
Here's an example of a tree:
```
          8
        /   \
       3     10
      / \      \
     1   6      14
        / \    /
       4   7  13
```

Trees in computer science grow upside down! Some vocabulary:
- Each item in the tree is stored in a **node**. The node at the top (8) is the **root**.
- The lines between nodes are called **edges** (or **branches**).
- The nodes directly below a node are its **children**, and the node directly above a node is its **parent**. For example, 3 is the parent of 1 and 6.
- A node with no children (like 1, 4, 7 and 13) is a **leaf**.
- Any node, together with everything below it, forms a **subtree**. For example, 3, 1, 6, 4 and 7 form the _left subtree_ of 8.
- The **height** of a tree is the number of edges on the longest path from the root down to a leaf. The tree above has height 3 (e.g. 8 → 3 → 6 → 4).

In a **binary tree**, each node has at most two children: a _left child_ and a _right child_.

## Binary search trees
A **binary search tree** (BST) is a binary tree that follows one extra rule: for every node, everything in its left subtree is _smaller_ than it, and everything in its right subtree is _larger_ than it. Check that the tree above follows this rule!

This rule makes searching very quick. To find out whether a value is in the tree, start at the root. If the value is smaller than the root, it can only be in the left subtree, so go left; if it's larger, it can only be in the right subtree, so go right. Repeat until you either find the value, or try to go somewhere there isn't a node (in which case the value isn't in the tree). For example, to search for 7 in the tree above: 7 < 8, so go left to 3; 7 > 3, so go right to 6; 7 > 6, so go right to 7. Found it, in just four steps!

To **insert** a value, we do exactly the same thing: follow the path the value would take if we were searching for it, and when we reach an empty space, put a new node there. Here's a binary search tree in Python:
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None   # the left child (None if there isn't one)
        self.right = None  # the right child (None if there isn't one)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Adds `value` to the tree"""
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
```

You can find this class in [`examples/binary_search_tree.py`](examples/binary_search_tree.py). (Values equal to an existing value go to the right here. Some BSTs don't allow duplicates at all.)

**Task 1:** On paper, draw the binary search tree you get by inserting these values, in this order, into an empty tree: 50, 30, 70, 20, 40, 60, 80, 35, 65. What is the height of the tree? Which nodes are leaves? Then draw the tree you get by inserting the same values in the order 20, 30, 35, 40, 50, 60, 65, 70, 80. What do you notice? [Solution](solutions/task1_drawing_trees.md)

**Task 2:** Add a method `contains(value)` to the `BinarySearchTree` class, which returns `True` if `value` is in the tree and `False` otherwise. Then add methods `minimum()` and `maximum()`, which return the smallest and largest values in the tree. Hint: where in the tree is the smallest value? [Solution](solutions/task2_contains_min_max.py)

## Traversing a tree
With a list, there's one obvious order to visit the items in: from start to end. With a tree, there are several. The three most common are all _depth-first_ traversals, which are easiest to write using recursion (see [Lesson 16](../16-recursion-stacks-and-queues)). They differ only in _when_ they visit each node, compared with its subtrees:
- **Pre-order:** visit the node, then traverse its left subtree, then its right subtree.
- **In-order:** traverse the left subtree, then visit the node, then traverse the right subtree.
- **Post-order:** traverse the left subtree, then the right subtree, then visit the node.

```python
def in_order(node):
    """Prints the values in the subtree starting at `node`, in order"""
    if node is None:
        return  # an empty subtree has nothing in it
    in_order(node.left)
    print(node.value)
    in_order(node.right)
```

For the tree at the top of this lesson, the traversals give:

| Traversal  | Order                          |
|------------|--------------------------------|
| Pre-order  | 8, 3, 1, 6, 4, 7, 10, 14, 13   |
| In-order   | 1, 3, 4, 6, 7, 8, 10, 13, 14   |
| Post-order | 1, 4, 7, 6, 3, 13, 14, 10, 8   |

Notice that an in-order traversal of a binary search tree visits the values in sorted order! Pre-order traversals are useful for copying a tree (you create each node before its children), and post-order traversals are useful for deleting a tree (you delete each node's children before the node itself).

A fourth option is a **breadth-first** traversal, which visits the nodes level by level: 8, 3, 10, 1, 6, 14, 4, 7, 13.

**Task 3:** Add `pre_order()`, `in_order()` and `post_order()` methods to your `BinarySearchTree` class, each of which returns a Python list of the values in that order. Hint: each method can call a recursive helper function, which takes a node and the list to add values to. Check your answers against the table above. [Solution](solutions/task3_traversals.py)

**Task 4:** Add a `height()` method, which returns the height of the tree. Hint: the height of a subtree is 1 more than the height of its taller child subtree. What should the height of an empty tree be? [Solution](solutions/task4_height.py)

## Deleting a node
Deleting a node from a binary search tree is trickier, because we need to keep the BST rule true afterwards. There are three cases:
1. **The node is a leaf.** Just remove it (set its parent's pointer to `None`).
2. **The node has one child.** Replace the node with its child (point the node's parent at the node's child).
3. **The node has two children.** Find the node's _in-order successor_: the smallest value in its right subtree (go right once, then left as far as possible). Copy the successor's value into the node, then delete the successor from the right subtree. (The successor never has a left child, so deleting it is always case 1 or 2.)

For example, deleting 3 from the tree at the top of the lesson (case 3): the smallest value in 3's right subtree is 4, so 4 replaces 3, and the old 4 node is removed.
```
          8                           8
        /   \                       /   \
       3     10                    4     10
      / \      \       ──►        / \      \
     1   6      14               1   6      14
        / \    /                      \    /
       4   7  13                       7  13
```

**Task 5:** Add a `delete(value)` method to your `BinarySearchTree` class, which handles all three cases. Test it by deleting a leaf, a node with one child, a node with two children, and the root, and check that an in-order traversal still gives the values in order after each deletion. Hint: this is easiest to write recursively, as a helper function that deletes a value from the subtree starting at a node, and returns the new root of that subtree. [Solution](solutions/task5_delete.py)

## Balanced and unbalanced trees
How fast is searching a binary search tree? Each step goes down one level, so in the worst case, searching takes as many steps as the height of the tree (plus one). In a nicely _balanced_ tree, where each node's subtrees are about the same size, each level holds twice as many nodes as the level above, so a tree with $n$ nodes has a height of about $\log_2 n$. Searching, inserting and deleting all take $O(\log n)$ time: a balanced tree holding a million values has a height of only about 20!

But if values are inserted in sorted order (as in the second part of Task 1), every new value goes to the right of the one before, and the tree becomes a long chain: effectively a linked list. Its height is $n - 1$, and searching takes $O(n)$ time. There are clever kinds of BST (such as _AVL trees_ and _red-black trees_) that rebalance themselves as items are added, but they're beyond the scope of these lessons.

**Task 6:** _Tree sort_ is a sorting algorithm that inserts every item in a list into a binary search tree, then reads them back out using an in-order traversal. Write a function `tree_sort(items)` using your `BinarySearchTree` class, and check that it gives the same answer as `sorted` for some random lists. [Solution](solutions/task6_tree_sort.py)

**⭐ Task 7:** Add a `breadth_first()` method to your `BinarySearchTree` class, which returns the values level by level, from left to right. Hint: use a queue (see [Lesson 16](../16-recursion-stacks-and-queues)). Start with the root in the queue. Then, until the queue is empty, dequeue a node, record its value, and enqueue its children. [Solution](solutions/task7_breadth_first.py)

**⭐ Task 8:** Insert the numbers from 1 to 1,000 into a binary search tree, first in a random order (use `random.shuffle`) and then in sorted order, and print the height of each tree. Then write a function `build_balanced(sorted_items)` that builds a perfectly balanced tree from a sorted list. Hint: the middle item should be the root, the middle of the left half should be the root's left child, and so on, recursively. What's the height of your balanced tree? (Watch out: what happens if you use your recursive `height` method from Task 4 on the tree built from the sorted numbers? Why?) [Solution](solutions/task8_balanced_trees.py)

---
[← Previous: Lesson 18](../18-linked-lists) | [Contents](../../README.md) | [Next: Lesson 20 →](../20-hash-tables-and-sets)
