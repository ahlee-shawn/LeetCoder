# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if not node:
            return [0, 0]
        left = self.helper(node.left)
        right = self.helper(node.right)
        rob = node.val + left[1] + right[1]
        not_rob = max(left) + max(right)
        return [rob, not_rob]
        
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root))