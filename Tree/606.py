# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""
        ans = ""
        
        def dfs(node, ans):
            ans += str(node.val)
            
            if node.left is None and node.right is None:
                return ans
            
            
            if node.left is not None:
                ans += '('
                ans = dfs(node.left, ans)
                ans += ')'
            else:
                ans += '()'
            
            if node.right is not None:
                ans += '('
                ans = dfs(node.right, ans)
                ans += ')'
            
            return ans
        ans = dfs(t, ans)
        
        return ans