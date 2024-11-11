# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree(root):
    if not root:
        return None
    root.right, root.left = root.left, root.right
    invertTree(root.right)
    invertTree(root.left)

    return root
        