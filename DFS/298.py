# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxLength = 1
        
    def dfs(self, node):
        if not node:
            return -1, 0
        leftVal, leftLength = self.dfs(node.left)
        rightVal, rightLength = self.dfs(node.right)
        if (leftVal - 1) == (rightVal - 1)  == node.val:
            nextLength = max(leftLength, rightLength) + 1
            self.maxLength = max(self.maxLength, nextLength)
            return node.val, nextLength
        elif (leftVal - 1) == node.val:
            nextLength = leftLength + 1
            self.maxLength = max(self.maxLength, nextLength)
            return node.val, nextLength
        elif (rightVal - 1) == node.val:
            nextLength = rightLength + 1
            self.maxLength = max(self.maxLength, nextLength)
            return node.val, nextLength
        else:            
            return node.val, 1
    
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxLength