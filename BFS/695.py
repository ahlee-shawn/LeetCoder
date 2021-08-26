class Solution:
    def bfs(self, grid, m, n, i, j):
        queue = deque()
        queue.append([i, j])
        cur_area = 0
        grid[i][j] = -1
        while queue:
            i, j = queue.popleft()
            # UP
            if i != 0 and grid[i-1][j] == 1:
                queue.append([i-1, j])
                grid[i-1][j] = -1
            # DOWN
            if i != m - 1 and grid[i+1][j] == 1:
                queue.append([i+1, j])
                grid[i+1][j] = -1
            # LEFT
            if j != 0 and grid[i][j-1] == 1:
                queue.append([i, j-1])
                grid[i][j-1] = -1
            #RIGHT
            if j != n - 1 and grid[i][j+1] == 1:
                queue.append([i, j+1])
                grid[i][j+1] = -1
            cur_area += 1
        return cur_area, grid
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_area, grid = self.bfs(grid, m, n, i, j)
                    print(i, j, cur_area)
                    max_area = max(max_area, cur_area)
        return max_area