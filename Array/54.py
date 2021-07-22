class Solution:
    def __init__(self):
        self.count = 0
        self.ans = []
        self.row_low = 0
        self.col_low = 0
        self.row_high = 0
        self.col_high = 0
        
    def helper(self, matrix, direction):
        if direction == 0: # move right
            for k in range(self.col_low, self.col_high):
                self.ans.append(matrix[self.row_low][k])
            self.count -= (self.col_high - self.col_low)
            self.row_low += 1
        elif direction == 1: # move down
            for k in range(self.row_low, self.row_high):
                self.ans.append(matrix[k][self.col_high-1])
            self.count -= (self.row_high - self.row_low)
            self.col_high -= 1
        elif direction == 2: # move left
            for k in range(self.col_high-1, self.col_low-1, -1):
                self.ans.append(matrix[self.row_high-1][k])
            self.count -= (self.col_high - self.col_low)
            self.row_high -= 1
        elif direction == 3: # move up
            for k in range(self.row_high-1 ,self.row_low-1, -1):
                self.ans.append(matrix[k][self.col_low])
            self.count -= (self.row_high - self.row_low)
            self.col_low += 1
            
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.row_high, self.col_high = len(matrix), len(matrix[0])
        self.count = self.row_high * self.col_high
        
        direction = 0
        
        while self.count > 0:
            self.helper(matrix, direction)
            direction += 1
            direction %= 4
        
        return self.ans