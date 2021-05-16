# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 1
        queue = deque()
        queue.append([root])
        while queue:
            curLevel = queue.popleft()
            nextLevel = []
            for curNode in curLevel:
                if curNode.left:
                    nextLevel.append(curNode.left)
                if curNode.right:
                    nextLevel.append(curNode.right)
                if not curNode.left and not curNode.right:
                    return level
            level += 1
            queue.append(nextLevel)
        return level