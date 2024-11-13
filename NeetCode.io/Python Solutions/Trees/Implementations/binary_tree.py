class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value, end=" ")
        if self.right:
            self.right.in_order_traversal()