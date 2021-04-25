# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self, node1, node2):
        if node1 and node2:
            node1.val += node2.val
        if node1.left:
            if node2.left:
                node1.left = self.merge(node1.left, node2.left)
        else:
            node1.left = node2.left
        
        if node1.right:
            if node2.right:
                node1.right = self.merge(node1.right, node2.right)
        else:
            node1.right = node2.right
        return node1
        
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        return self.merge(root1, root2)

# Cleaner Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        node1.val += node2.val
        node1.left = self.merge(node1.left, node2.left)
        node1.right = self.merge(node1.right, node2.right)
        return node1
        
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        return self.merge(root1, root2)