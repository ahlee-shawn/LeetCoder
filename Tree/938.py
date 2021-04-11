# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, low, high, current_sum):
        if low <= root.val <= high:
            current_sum += root.val
        if root.left:
            current_sum = self.dfs(root.left, low, high, current_sum)
        if root.right:
            current_sum = self.dfs(root.right, low, high, current_sum)
        return current_sum
        
        
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return self.dfs(root, low, high, 0)