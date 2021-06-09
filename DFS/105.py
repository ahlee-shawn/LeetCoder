# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        newNode = TreeNode(val = preorder[0])
        inorderI = inorder.index(preorder[0])
        newNode.left = self.buildTree(preorder[1:inorderI+1], inorder[:inorderI])
        newNode.right = self.buildTree(preorder[inorderI+1:], inorder[inorderI+1:])
        return newNode