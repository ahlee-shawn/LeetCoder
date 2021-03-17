# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        num = root.val
        ans = True
        def bfs(num, queue, ans):
            if len(queue) == 0:
                return ans
            current = queue.pop(0)
            if current.val != num:
                ans = False
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            return bfs(num, queue, ans)
            
        queue = [root]
        return bfs(num, queue, ans)