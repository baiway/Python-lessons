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

    def contains(self, value):
        """Returns `True` if `value` is in the tree"""
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def minimum(self):
        """Returns the smallest value: keep going left until you can't"""
        if self.root is None:
            raise ValueError("The tree is empty")
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def maximum(self):
        """Returns the largest value: keep going right until you can't"""
        if self.root is None:
            raise ValueError("The tree is empty")
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value


tree = BinarySearchTree()
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(value)

print(tree.contains(7))    # True
print(tree.contains(5))    # False
print(tree.minimum())      # 1
print(tree.maximum())      # 14
