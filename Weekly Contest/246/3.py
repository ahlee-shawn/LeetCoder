# Count Sub Islands
class Solution:
    def dfs(self, grid, i, j, count):
        grid[i][j] = count
        # up
        if i > 0 and grid[i-1][j] == 1:
            self.dfs(grid, i-1, j, count)
        # down
        if i < len(grid)-1 and grid[i+1][j] == 1:
            self.dfs(grid, i+1, j, count)
        # left
        if j > 0 and grid[i][j-1] == 1:
            self.dfs(grid, i, j-1, count)
        #right
        if j < len(grid[0])-1 and grid[i][j+1] == 1:
            self.dfs(grid, i, j+1, count)
            
    def dfs2(self, grid1, grid2, i, j, count):
        if grid1[i][j] != count:
            return False
        grid2[i][j] = count
        temp1 = temp2 = temp3 = temp4 = True
        # up
        if i > 0 and grid2[i-1][j] == 1:
            temp1 = self.dfs2(grid1, grid2, i-1, j, count)
        # down
        if i < len(grid2)-1 and grid2[i+1][j] == 1:
            temp2 = self.dfs2(grid1, grid2, i+1, j, count)
        # left
        if j > 0 and grid2[i][j-1] == 1:
            temp3 = self.dfs2(grid1, grid2, i, j-1, count)
        #right
        if j < len(grid2[0])-1 and grid2[i][j+1] == 1:
            temp4 = self.dfs2(grid1, grid2, i, j+1, count)
        return temp1 and temp2 and temp3 and temp4
        
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # find islands in grid1
        count = -1
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 1:
                    self.dfs(grid1, i, j, count)
                    count -= 1
        # find island in grid2
        ans = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] < 0 and grid2[i][j] == 1:
                    temp = self.dfs2(grid1, grid2, i, j, grid1[i][j])
                    if temp:
                        ans += 1
        return ans