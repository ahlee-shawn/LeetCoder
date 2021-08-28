class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        table = [[0 for _ in range(n)] for _ in range(m)]
        # Row-wise
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    enemyCount = 0
                    # Enemy to the left of current cell
                    for k in range(0, j):
                        if grid[i][k] == 'E':
                            enemyCount += 1
                        elif grid[i][k] == 'W':
                            enemyCount = 0
                    table[i][j] += enemyCount
                    # Enemy to the right of current cell
                    enemyCount = 0
                    encounterWall = False
                    for k in range(j+1, n):
                        if grid[i][k] == 'E':
                            enemyCount += 1
                        elif grid[i][k] == 'W':
                            table[i][j] += enemyCount
                            encounterWall = True
                            break
                    if not encounterWall:
                        table[i][j] += enemyCount
        # Column-wise
        for j in range(n):
            for i in range(m):
                if grid[i][j] == '0':
                    enemyCount = 0
                    # Enemy above current cell
                    for k in range(0, i):
                        if grid[k][j] == 'E':
                            enemyCount += 1
                        elif grid[k][j] == 'W':
                            enemyCount = 0
                    table[i][j] += enemyCount
                    # Enemy below current cell
                    enemyCount = 0
                    encounterWall = False
                    for k in range(i+1, m):
                        if grid[k][j] == 'E':
                            enemyCount += 1
                        elif grid[k][j] == 'W':
                            table[i][j] += enemyCount
                            encounterWall = True
                            break
                    if not encounterWall:
                        table[i][j] += enemyCount
        maxValue = 0
        for i in range(m):
            for j in range(n):
                maxValue = max(maxValue, table[i][j])
        return maxValue