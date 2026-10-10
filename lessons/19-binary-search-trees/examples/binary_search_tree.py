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


def in_order(node):
    """Prints the values in the subtree starting at `node`, in order"""
    if node is None:
        return  # an empty subtree has nothing in it
    in_order(node.left)
    print(node.value)
    in_order(node.right)


tree = BinarySearchTree()
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(value)

in_order(tree.root)  # prints the values in sorted order
