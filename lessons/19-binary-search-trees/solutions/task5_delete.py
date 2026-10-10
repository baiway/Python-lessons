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

    def delete(self, value):
        """Removes `value` from the tree"""
        self.root = _delete(self.root, value)

    def in_order(self):
        values = []
        _in_order(self.root, values)
        return values


def _delete(node, value):
    """Deletes `value` from the subtree starting at `node`, and returns the new
    root of that subtree"""
    if node is None:
        raise ValueError(f"{value} is not in the tree")

    if value < node.value:
        node.left = _delete(node.left, value)
        return node
    if value > node.value:
        node.right = _delete(node.right, value)
        return node

    # We've found the node to delete. Cases 1 and 2: it has at most one child,
    # so replace it with that child (or with None, if it's a leaf)
    if node.left is None:
        return node.right
    if node.right is None:
        return node.left

    # Case 3: it has two children. Find the smallest value in the right
    # subtree, copy it here, then delete it from the right subtree.
    successor = node.right
    while successor.left is not None:
        successor = successor.left
    node.value = successor.value
    node.right = _delete(node.right, successor.value)
    return node


def _in_order(node, values):
    if node is None:
        return
    _in_order(node.left, values)
    values.append(node.value)
    _in_order(node.right, values)


tree = BinarySearchTree()
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(value)
print(tree.in_order())

for value in [13, 14, 3, 8]:  # a leaf, a node with one child, two children, the root
    tree.delete(value)
    print(f"After deleting {value}: {tree.in_order()}")

try:
    tree.delete(42)
except ValueError as error:
    print(f"Error: {error}")
