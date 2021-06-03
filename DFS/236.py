# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    def dfs(self, node, p, q):
        if self.ans:
            return -1
        if not node:
            return 0
        mid = 0
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        if node == p:
            mid = 1
        if node == q:
            mid = 1
        if mid + left + right >= 2 and not self.ans:
            self.ans = node
        return mid + left + right
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.ans