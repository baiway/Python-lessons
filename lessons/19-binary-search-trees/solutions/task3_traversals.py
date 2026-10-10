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

    def pre_order(self):
        values = []
        _pre_order(self.root, values)
        return values

    def in_order(self):
        values = []
        _in_order(self.root, values)
        return values

    def post_order(self):
        values = []
        _post_order(self.root, values)
        return values


def _pre_order(node, values):
    if node is None:
        return
    values.append(node.value)
    _pre_order(node.left, values)
    _pre_order(node.right, values)


def _in_order(node, values):
    if node is None:
        return
    _in_order(node.left, values)
    values.append(node.value)
    _in_order(node.right, values)


def _post_order(node, values):
    if node is None:
        return
    _post_order(node.left, values)
    _post_order(node.right, values)
    values.append(node.value)


tree = BinarySearchTree()
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(value)

print(tree.pre_order())   # [8, 3, 1, 6, 4, 7, 10, 14, 13]
print(tree.in_order())    # [1, 3, 4, 6, 7, 8, 10, 13, 14]
print(tree.post_order())  # [1, 4, 7, 6, 3, 13, 14, 10, 8]
