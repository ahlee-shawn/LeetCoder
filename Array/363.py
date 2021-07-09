
# TLE
class Solution:
    def maxSumSubmatrix(self, M: List[List[int]], k: int) -> int:
        m = len(M)
        n = len(M[0])
        matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1] + M[i-1][j-1]

        print(matrix)
        max_area = float('-inf')

        for row in range(1, m+1):
            for col in range(1, n+1):
                for i in range(row):
                    for j in range(col):
                        area = matrix[row][col] - matrix[row][j] - matrix[i][col] + matrix[i][j]
                        if area > max_area and area <= k:
                            max_area = area
                
        return max_area

