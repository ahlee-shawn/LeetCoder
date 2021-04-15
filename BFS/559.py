"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            for i in range(len(queue)):
                current_node = queue.popleft()
                if current_node.children:
                    for child in current_node.children:
                        queue.append(child)
            depth += 1
        return depth