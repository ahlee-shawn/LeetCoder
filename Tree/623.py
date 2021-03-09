# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_node = TreeNode(val=v, left=root, right=None)
            return new_node
        queue = [[root]]
        current_level = 0
        while queue:
            current_level_nodes = queue.pop(0)
            next_level_nodes = []
            for current_node in current_level_nodes:
                if current_node.left:
                    next_level_nodes.append(current_node.left)
                if current_node.right:
                    next_level_nodes.append(current_node.right)
            queue.append(next_level_nodes)
            current_level += 1
            if current_level == d - 1:
                for current_node in current_level_nodes:
                    new_node = TreeNode(val=v, left=current_node.left, right=None)
                    current_node.left = new_node
                    new_node = TreeNode(val=v, left=None, right=current_node.right)
                    current_node.right = new_node
                return root
        