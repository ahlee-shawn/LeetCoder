import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convert(self, nums, low, high):
        if low > high:
            return None
        mid = math.ceil((low + high)/2)
        root = TreeNode(val=nums[mid])
        root.left = self.convert(nums, low, mid-1)
        root.right = self.convert(nums, mid+1, high)
        return root
        
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.convert(nums, 0, len(nums)-1)