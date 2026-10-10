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

    def in_order(self):
        values = []
        _in_order(self.root, values)
        return values


def _in_order(node, values):
    if node is None:
        return
    _in_order(node.left, values)
    values.append(node.value)
    _in_order(node.right, values)


def tree_sort(items):
    """Returns a sorted copy of `items`, using a binary search tree"""
    tree = BinarySearchTree()
    for item in items:
        tree.insert(item)
    return tree.in_order()


for i in range(5):
    items = [random.randint(1, 100) for _ in range(20)]
    print(tree_sort(items) == sorted(items))  # True

print(tree_sort(["pear", "apple", "fig", "banana"]))
