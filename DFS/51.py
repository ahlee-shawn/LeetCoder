class Solution:
    def convert(self, state):
        board = []
        for row in state:
            board.append("".join(row))
        return board
        
    def helper(self, n, ans, curRow, colSet, diagSet, antiDiagSet, state):
        if curRow == n:
            ans.append(self.convert(state))
        else:
            for col in range(n):
                diag, antiDiag = curRow-col, curRow+col
                if col not in colSet and diag not in diagSet and antiDiag not in antiDiagSet:
                    state[curRow][col] = 'Q'
                    colSet.add(col)
                    diagSet.add(diag)
                    antiDiagSet.add(antiDiag)
                    self.helper(n, ans, curRow+1, colSet, diagSet, antiDiagSet, state)
                    state[curRow][col] = '.'
                    colSet.remove(col)
                    diagSet.remove(diag)
                    antiDiagSet.remove(antiDiag)
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        emptyBoard = [['.' for _ in range(n)] for _ in range(n)]
        self.helper(n, ans, 0, set(), set(), set(), emptyBoard)
        return ans