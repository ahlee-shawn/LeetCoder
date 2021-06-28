# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    
    def dfs(self, node, prev):
        prev = prev * 10 + node.val
        if not (node.left or node.right):
            self.ans += prev
            return
        if node.left:
            self.dfs(node.left, prev)
        if node.right:
            self.dfs(node.right, prev)
        
    def sumNumbers(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.ans