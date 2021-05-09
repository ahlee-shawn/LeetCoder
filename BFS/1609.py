# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = deque()
        queue.append([root])
        even = True
        while queue:
            curLevel = queue.popleft()
            curLevelValue = []
            nextLevel = []
            for node in curLevel:
                if not even and node.val % 2:
                    return False
                if even and not node.val % 2:
                    return False
                curLevelValue.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if even:
                for i in range(len(curLevelValue)-1):
                    if curLevelValue[i] >= curLevelValue[i+1]:
                        return False
            else:
                for i in range(len(curLevelValue)-1, 0, -1):
                    if curLevelValue[i] >= curLevelValue[i-1]:
                        return False
            even = not even
            if nextLevel != []:
                queue.append(nextLevel)
        return True