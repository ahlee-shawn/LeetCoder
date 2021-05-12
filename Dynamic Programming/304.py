class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.arr = [[0 for _ in range(n)] for _ in range(m)]
        preSum = 0
        for i in range(n):
            self.arr[0][i] = preSum + matrix[0][i]
            preSum += matrix[0][i]
        preSum = 0
        for i in range(m):
            self.arr[i][0] = preSum + matrix[i][0]
            preSum += matrix[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                self.arr[i][j] = self.arr[i-1][j] + self.arr[i][j-1] - self.arr[i-1][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == col1 == 0:
            return self.arr[row2][col2]
        elif row1 == 0:
            return self.arr[row2][col2] - self.arr[row2][col1-1]
        elif col1 == 0:
            return self.arr[row2][col2] - self.arr[row1-1][col2]
        elif row1 > 0 and col1 > 0:
            return self.arr[row2][col2] - self.arr[row1-1][col2] - self.arr[row2][col1-1] + self.arr[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)