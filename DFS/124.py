# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._maxPathSum = float(-inf)
        
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if node.val > self._maxPathSum:
            self._maxPathSum = node.val
        if left + node.val > self._maxPathSum:
            self._maxPathSum = left + node.val
        if right + node.val > self._maxPathSum:
            self._maxPathSum = right + node.val
        if left + right + node.val > self._maxPathSum:
            self._maxPathSum = left + right + node.val
        return max(max(left, right) + node.val, node.val)
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self._maxPathSum
        