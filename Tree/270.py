# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.closestVal = 0
        self.difference = float('inf')
        
    def dfs(self, root, target):
        if not root:
            return
        currentDifference = abs(root.val - target)
        if currentDifference < self.difference:
            self.closestVal = root.val
            self.difference = currentDifference
        if target <= root.val:
            self.dfs(root.left, target)
        else:
            self.dfs(root.right, target)
        
        
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.dfs(root, target)
        return self.closestVal