# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        
    def dfs(self, root, to_delete_set, hasParent):
        if root is None:
            return None
        
        if root.val in to_delete_set:
            root.left = self.dfs(root.left, to_delete_set, False)
            root.right = self.dfs(root.right, to_delete_set, False)
            return None
        else:
            if not hasParent:
                self.result.append(root)
            root.left = self.dfs(root.left, to_delete_set, True)
            root.right = self.dfs(root.right, to_delete_set, True)
        
            return root
        
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result = []
        self.dfs(root, set(to_delete), False)
        return self.result

