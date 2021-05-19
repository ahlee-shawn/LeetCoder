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