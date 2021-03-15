# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        answer, path = [], []
        def dfs(current_node, partial_sum, path):
            path.append(current_node)
            if current_node.left:
                path = dfs(current_node.left, partial_sum-current_node.val, path)
                path.pop(-1)
            if current_node.right:
                path = dfs(current_node.right, partial_sum-current_node.val, path)
                path.pop(-1)
            if current_node.left is None and current_node.right is None and current_node.val == partial_sum:
                new_path = []
                for node in path:
                    new_path.append(node.val)
                answer.append(new_path)
                return path
            return path
        dfs(root, targetSum, path)
        return answer