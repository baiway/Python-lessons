import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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

    def height(self):
        """Returns the height of the tree, by counting the levels one at a time.

        The recursive version from Task 4 doesn't work here: when the values
        are inserted in sorted order, the tree is 999 levels deep, which is
        more than Python's recursion limit (see Lesson 16). So instead, we
        work through the tree level by level, using a loop."""
        if self.root is None:
            return -1
        level = [self.root]
        height = -1
        while len(level) > 0:
            height = height + 1
            next_level = []
            for node in level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            level = next_level
        return height


def build_balanced(sorted_items):
    """Builds a balanced binary search tree from a sorted list"""
    tree = BinarySearchTree()
    tree.root = _build(sorted_items)
    return tree


def _build(items):
    """Returns the root of a balanced subtree containing `items`"""
    if len(items) == 0:
        return None
    mid = len(items) // 2
    node = TreeNode(items[mid])
    node.left = _build(items[:mid])
    node.right = _build(items[mid + 1:])
    return node


numbers = list(range(1, 1001))

shuffled = numbers.copy()
random.shuffle(shuffled)
random_tree = BinarySearchTree()
for n in shuffled:
    random_tree.insert(n)
print(f"Height when inserted in a random order: {random_tree.height()}")  # usually around 20

sorted_tree = BinarySearchTree()
for n in numbers:
    sorted_tree.insert(n)
print(f"Height when inserted in sorted order: {sorted_tree.height()}")  # 999

balanced = build_balanced(numbers)
print(f"Height when built balanced: {balanced.height()}")  # 9, since 2^10 = 1024 > 1000
