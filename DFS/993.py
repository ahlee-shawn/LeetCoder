'''
BFS
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, x, y, table, parent_val, level):
        if root.val in (x,y):
            table[root.val] = [parent_val, level]
        if root.left:
            self.dfs(root.left, x, y, table, root.val, level+1)
        if root.right:
            self.dfs(root.right, x, y, table, root.val, level+1)
        return table
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        table = {}
        table = self.dfs(root, x, y, table, None, 0)
        return table[x][1] == table[y][1] and table[x][0] != table[y][0]

'''
BFS
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        table = {}
        queue = deque()
        queue.append(root)
        level = 1
        if root.val in (x, y):
            return False
        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()
                for child in (current_node.left, current_node.right):
                    if child:
                        if child.val in (x, y):
                            table[child.val] = [current_node.val, level]
                        queue.append(child)
            level += 1
        return table[x][1] == table[y][1] and table[x][0] != table[y][0]