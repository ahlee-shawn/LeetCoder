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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def rob(self, root: TreeNode) -> int:
        robbed_table = {}
        not_robbed_table = {}
        
        def helper(node, parent_robbed):
            if not node:
                return 0

            if parent_robbed:
                if node in robbed_table:
                    return robbed_table[node]
                else:
                    result = helper(node.left, False) + helper(node.right, False)
                    robbed_table[node] = result
                    return result
            else:
                if node in not_robbed_table:
                    return not_robbed_table[node]
                else:
                    robbed = node.val + helper(node.left, True) + helper(node.right, True)
                    not_robbed = helper(node.left, False) + helper(node.right, False)
                    result = max(robbed, not_robbed)
                    not_robbed_table[node] = result
                    return result
        
        return helper(root, False)