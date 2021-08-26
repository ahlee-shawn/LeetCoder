# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_length = 0
        
    def dfs(self, node):
        if not node:
            return 0
        else:
            left = self.dfs(node.left)
            right = self.dfs(node.right)
            self.max_length = max(self.max_length, left + right)
            return max(left, right) + 1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.max_length