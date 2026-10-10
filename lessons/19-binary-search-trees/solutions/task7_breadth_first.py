from collections import deque

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

    def breadth_first(self):
        """Returns the values level by level, from left to right"""
        values = []
        if self.root is None:
            return values

        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            values.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return values


tree = BinarySearchTree()
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(value)
print(tree.breadth_first())  # [8, 3, 10, 1, 6, 14, 4, 7, 13]
