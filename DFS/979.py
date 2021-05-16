# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        
    def dfs(self, node):
        if not node:
            return 0
        leftChild = self.dfs(node.left)
        rightChild = self.dfs(node.right)
        self.ans += abs(leftChild) + abs(rightChild)
        return node.val + leftChild + rightChild - 1
        
    def distributeCoins(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans