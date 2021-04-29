# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, current_path, path_list):
        if not node.left and not node.right:
            current_path += str(node.val)
            path_list.append(current_path)
            return path_list
        else:
            current_path += (str(node.val)+"->")
            if node.left:
                path_list = self.dfs(node.left, current_path, path_list)
            if node.right:
                path_list = self.dfs(node.right, current_path, path_list)
            return path_list
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        return self.dfs(root, "", [])