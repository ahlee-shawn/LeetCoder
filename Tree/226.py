# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, root):
        root.left, root.right = root.right, root.left
        if root.left:
            self.recursive(root.left)
        if root.right:
            self.recursive(root.right)
        return root
        
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        return self.recursive(root)