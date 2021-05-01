class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0 for _ in range(n)] for _ in range(m)]
        table[0][0] = 1
        for j in range(1, n):
            table[0][j] += 1
        for i in range(1, m):
            table[i][0] += 1
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] += (table[i-1][j] + table[i][j-1])
        return table[-1][-1]