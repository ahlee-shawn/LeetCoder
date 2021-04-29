class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        table = [[0 for _ in range(n)] for _ in range(m)]
        if not obstacleGrid[0][0]:
            table[0][0] = 1
        for j in range(1, n):
            if not obstacleGrid[0][j]:
                table[0][j] += table[0][j-1]
        for i in range(1, m):
            if not obstacleGrid[i][0]:
                table[i][0] += table[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    table[i][j] += (table[i-1][j] + table[i][j-1])
        return table[-1][-1]