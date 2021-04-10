'''
BFS + Memorization
'''
class Solution:
    def find_path(self, table, i, j, m, n):
        if i == m and j == n:
            return 1
        if table[i][j] == -1:
            down = right = 0
            if i < m:
                down = self.find_path(table, i+1, j, m, n)
            if j < n:
                right = self.find_path(table, i, j+1, m, n)
            table[i][j] = down + right
        return table[i][j]
        
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[-1 for _ in range(n)] for _ in range(m)]
        return self.find_path(table, 0, 0, m-1, n-1)

'''
Simple Math
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        ans = 1
        for i in range(max(m, n)+1, m+n+1):
            ans *= i
        for i in range(1, min(m, n)+1):
            ans /= i
        return int(ans)