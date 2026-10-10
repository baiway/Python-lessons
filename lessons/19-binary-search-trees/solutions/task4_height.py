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
        """Returns the number of edges on the longest path from the root to a leaf"""
        return _height(self.root)


def _height(node):
    # An empty tree has a height of -1, so that a tree with just a root (and
    # no edges) has a height of 0
    if node is None:
        return -1
    return 1 + max(_height(node.left), _height(node.right))


tree = BinarySearchTree()
print(tree.height())  # -1 (an empty tree)
tree.insert(8)
print(tree.height())  # 0 (just the root)
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13][1:]:
    tree.insert(value)
print(tree.height())  # 3
