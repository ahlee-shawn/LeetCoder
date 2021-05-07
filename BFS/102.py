# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        queue = deque()
        if root:
            queue.append([root])
        while queue:
            curLevelNode = queue.popleft()
            curLevelVal, nextLevelNode = [], []
            for node in curLevelNode:
                curLevelVal.append(node.val)
                if node.left:
                    nextLevelNode.append(node.left)
                if node.right:
                    nextLevelNode.append(node.right)
            ans.append(curLevelVal)
            if nextLevelNode:
                queue.append(nextLevelNode)
        return ans