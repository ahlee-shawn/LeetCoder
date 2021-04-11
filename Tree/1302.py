# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = deque()
        queue.append(root)
        ans = 0
        while queue:
            ans = 0
            has_child = False
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if current_node.left:
                    queue.append(current_node.left)
                    has_child = True
                if current_node.right:
                    queue.append(current_node.right)
                    has_child = True
                if not has_child:
                    ans += current_node.val
        return ans