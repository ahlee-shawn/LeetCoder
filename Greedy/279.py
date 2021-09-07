class Solution:
    def __init__(self):
        self.table = dict()
        self.table[0] = 0

    def dfs(self, square_num, index, n):
        if n in self.table:
            return self.table[n]
        else:
            # n = 12, index = 1
            counter = n // square_num[index]
            temp = self.dfs(square_num, index + 1, n - counter * square_num[index])
            self.table[n] = counter + temp
            return self.table[n]
            
    def numSquares(self, n: int) -> int:
        # n = 12
        square_num = [0 for _ in range(sqrt(n))] # [0, 0, 0]
        for i in range(sqrt(n)):
            square_num[i] = (i+1) * (i+1)
        # [1,4,9]
        square_num = square_num[::-1] # [9, 4, 1]
        ans = float('inf')
        for i in range(len(square_num)):
            ans = min(ans, self.dfs(square_num, i, n))
        return ans
