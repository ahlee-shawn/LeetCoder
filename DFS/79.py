# Faster
class Solution:
    def dfs(self, board, word, i, j, index):
        if index == len(word) - 1 and board[i][j] == word[index]:
            return True
        else:
            up = down = left = right = False
            # Up
            if i > 0 and board[i-1][j] == word[index+1]:
                tmp = board[i][j]
                board[i][j] = '#'
                up = self.dfs(board, word, i-1, j, index+1)
                board[i][j] = tmp
            # Down
            if i < len(board)-1 and board[i+1][j] == word[index+1]:
                tmp = board[i][j]
                board[i][j] = '#'
                down = self.dfs(board, word, i+1, j, index+1)
                board[i][j] = tmp
            # Left
            if j > 0 and board[i][j-1] == word[index+1]:
                tmp = board[i][j]
                board[i][j] = '#'
                left = self.dfs(board, word, i, j-1, index+1)
                board[i][j] = tmp
            # Right
            if j < len(board[0])-1 and board[i][j+1] == word[index+1]:
                tmp = board[i][j]
                board[i][j] = '#'
                right = self.dfs(board, word, i, j+1, index+1)
                board[i][j] = tmp
            return up or down or left or right
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    tmp = self.dfs(board, word, i, j, 0)
                    if tmp:
                        return True
        return False

class Solution:
    def dfs(self, board, word, row, col, i):
        if row == -1 or row == len(board) or col == -1 or col == len(board[0]):
            return False
        if board[row][col] != word[i]:
            return False
        if board[row][col] == word[i] and i == len(word)-1:
            return True
        tmp = board[row][col]
        board[row][col] = '*'
        left = self.dfs(board, word, row, col-1, i+1)
        right = self.dfs(board, word, row, col+1, i+1)
        up = self.dfs(board, word, row-1, col, i+1)
        down = self.dfs(board, word, row+1, col, i+1)
        board[row][col] = tmp
        return left or right or up or down
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.dfs(board, word, row, col, 0):
                        return True
        return False