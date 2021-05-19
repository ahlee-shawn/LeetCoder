class Solution:
    def dfs(self, grid, row, col):
        if row == -1 or row == len(grid) or col == -1 or col == len(grid[0]):
            return 0
        if grid[row][col] == 0:
            return 0
        tmp = grid[row][col]
        grid[row][col] = 0
        up = self.dfs(grid, row-1, col)
        down = self.dfs(grid, row+1, col)
        left = self.dfs(grid, row, col-1)
        right = self.dfs(grid, row, col+1)
        grid[row][col] = tmp
        return grid[row][col] + max(up, down, left, right)
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    ans = max(ans, self.dfs(grid, row, col))
        return ans