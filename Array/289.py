        class Solution:
    def check(self, board, m, n, i, j):
        live_neighbor = 0
        if i > 0:
            if j > 0 and board[i-1][j-1] % 2:
                live_neighbor += 1
            if board[i-1][j] % 2:
                live_neighbor += 1
            if j < n - 1 and board[i-1][j+1] % 2:
                live_neighbor += 1
        if j > 0 and board[i][j-1] % 2:
            live_neighbor += 1
        if j < n - 1 and board[i][j+1] % 2:
            live_neighbor += 1
        if i < m - 1:
            if j > 0 and board[i+1][j-1] % 2:
                live_neighbor += 1
            if board[i+1][j] % 2:
                live_neighbor += 1
            if j < n - 1 and board[i+1][j+1] % 2:
                live_neighbor += 1
        if board[i][j] % 2:
            if live_neighbor < 2 or live_neighbor > 3:
                board[i][j] = 5
            else:
                board[i][j] = 3
        else:
            if live_neighbor == 3:
                board[i][j] = 2
            else:
                board[i][j] = 4
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.check(board, m, n, i, j)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] <= 3:
                    board[i][j] = 1
                else:
                    board[i][j] = 0