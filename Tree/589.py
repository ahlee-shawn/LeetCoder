"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            current_node = stack.pop(-1)
            ans.append(current_node.val)
            for child in reversed(current_node.children):
                if child:
                    stack.append(child)
        return ans