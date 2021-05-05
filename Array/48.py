class Solution:
    def transpose(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i+1, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        
    def reverse(self, A):
        n = len(A)
        for i in range(n):
            for j in range(n//2):
                A[i][j], A[i][n-j-1] = A[i][n-j-1], A[i][j]
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reverse(matrix)