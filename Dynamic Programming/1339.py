# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.midPoint = -1
        
    def dfs(self, node, target=None):
        if not node:
            return 0
        left = self.dfs(node.left, target)
        right = self.dfs(node.right, target)
        partialSum = left + right + node.val
        if target:
            if abs(partialSum - target) < abs(self.midPoint - target):
                self.midPoint = partialSum
        return partialSum
        
    def maxProduct(self, root: TreeNode) -> int:
        totalSum = self.dfs(root)
        print(totalSum)
        self.dfs(root, totalSum//2)
        print(self.midPoint)
        return (self.midPoint*(totalSum-self.midPoint)) % (10**9+7)