# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        level = 0
        level_count = []
        
        def dfs(node, level, level_count, ans):
            if node is None:
                return level_count, ans
            if len(ans) == level:
                ans.append(0)
                level_count.append(0)
            ans[level] += node.val
            level_count[level] += 1
            
            level_count, ans = dfs(node.left, level+1, level_count, ans)
            level_count, ans = dfs(node.right, level+1, level_count, ans)
            return level_count, ans
            
        level_count, ans = dfs(root, level, level_count, ans)
        for i in range(len(ans)):
            ans[i] = ans[i]/level_count[i]
        return ans