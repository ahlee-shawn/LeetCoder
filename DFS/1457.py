# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        self.values = [0 for _ in range(9)]
        
    def dfs(self, node):
        if not node:
            return
        self.values[node.val-1] += 1
        if not node.left and not node.right:
            odd = 0
            for i in range(9):
                if self.values[i] % 2:
                    odd += 1
            if odd < 2:
                self.ans += 1
        else:
            self.dfs(node.left)
            self.dfs(node.right)
        self.values[node.val-1] -= 1
        
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans