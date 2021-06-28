# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minDiff = float('inf')
        self.prev = float('-inf')
        
    def dfs(self, node):
        if node.left:
            self.dfs(node.left)
        self.minDiff = min(self.minDiff, node.val - self.prev)
        self.prev = node.val
        if node.right:
            self.dfs(node.right)
        
    def minDiffInBST(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.minDiff
        