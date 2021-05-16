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
        # state = -1 -> leaf
        # state = 2 -> camera's parent
        # state = 1 -> camera
        # state = 0 -> camera's child
        if not node:
            return -1
        L = self.dfs(node.left)
        R = self.dfs(node.right)
        if L == 0 or R == 0:
            self.ans += 1
            return 1
        if L == 1 or R == 1:
            return 2
        if L == R == -1 or L == 2 or R == 2:
            return 0
        
    def minCameraCover(self, root: TreeNode) -> int:
        state = self.dfs(root)
        if state == 0 :
            self.ans += 1
        return self.ans