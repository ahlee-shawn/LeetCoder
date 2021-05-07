# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        queue = deque()
        if root:
            queue.append([root])
        even = True
        while queue:
            curLevelNode = queue.popleft()
            curLevelVal, nextLevelNode = [], []
            for i in range(len(curLevelNode)-1, -1, -1):
                curLevelVal.append(curLevelNode[i].val)
                if even:
                    if curLevelNode[i].left:
                        nextLevelNode.append(curLevelNode[i].left)
                    if curLevelNode[i].right:
                        nextLevelNode.append(curLevelNode[i].right)
                else:
                    if curLevelNode[i].right:
                        nextLevelNode.append(curLevelNode[i].right)
                    if curLevelNode[i].left:
                        nextLevelNode.append(curLevelNode[i].left)
            ans.append(curLevelVal)
            if nextLevelNode:
                queue.append(nextLevelNode)
            even = not even
        return ans