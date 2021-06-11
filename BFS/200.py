class Solution:
    def findIslandsBFS(self, grid, i, j):
        # BFS
        queue = deque()
        queue.append([i, j])
        while queue:
            curI, curJ = queue.popleft()
            if grid[curI][curJ] == "1": # 2: curI && cur J has been visited
                grid[curI][curJ] = "2"
                # UP
                if curI > 0:
                    queue.append([curI-1, curJ])
                # Down
                if curI < len(grid) - 1:
                    queue.append([curI+1, curJ])
                # Left
                if curJ > 0:
                    queue.append([curI, curJ-1])
                # Right
                if curJ < len(grid[0]) - 1:
                    queue.append([curI, curJ+1])

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.findIslandsBFS(grid, i, j)
                    ans += 1
        return ans