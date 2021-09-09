"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque()
        if root:
            queue.append([root])
        while queue:
            next_level = []
            current_level = queue.popleft()
            n = len(current_level)
            for i in range(n):
                current_node = current_level[i]
                if current_node.left:
                    next_level.append(current_node.left)
                if current_node.right:
                    next_level.append(current_node.right)
                if i == n - 1:
                    current_node.next = None
                else:
                    current_node.next = current_level[i+1]
            if next_level:
                queue.append(next_level)
        return root