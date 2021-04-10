class Solution:
        
    def find_longest_increasing_path_starting_with_index(self, matrix, table, i, j, m, n):
        if table[i][j] == -1:
            current_max = 0
            # UP
            if i != 0 and matrix[i][j] > matrix[i-1][j]:
                current = self.find_longest_increasing_path_starting_with_index(matrix, table, i-1, j, m, n) + 1
                current_max = max(current_max, current)
            # DOWN
            if i != m-1 and matrix[i][j] > matrix[i+1][j]:
                current = self.find_longest_increasing_path_starting_with_index(matrix, table, i+1, j, m, n) + 1
                current_max = max(current_max, current)
            # LEFT
            if j != 0 and matrix[i][j] > matrix[i][j-1]:
                current = self.find_longest_increasing_path_starting_with_index(matrix, table, i, j-1, m, n) + 1
                current_max = max(current_max, current)
            # RIGHT
            if j != n-1 and matrix[i][j] > matrix[i][j+1]:
                current = self.find_longest_increasing_path_starting_with_index(matrix, table, i, j+1, m, n) + 1
                current_max = max(current_max, current)
            table[i][j] = current_max
        return table[i][j]
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        table = [ [-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.find_longest_increasing_path_starting_with_index(matrix, table, i, j, m, n)
        ans = 0
        for i in range(m):
            for j in range(n):
                if table[i][j] > ans:
                    ans = table[i][j]
        return ans+1