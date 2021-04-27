# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isIdentical(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isIdentical(s.left, t.left) and self.isIdentical(s.right, t.right)
            
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        stack = deque()
        stack.append(s)
        while stack:
            current_node = stack.pop()
            current_result = self.isIdentical(current_node, t)
            if current_result:
                return True
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
        return False