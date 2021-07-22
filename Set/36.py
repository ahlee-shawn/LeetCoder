class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowTable = [set() for _ in range(9)]
        colTable = [set() for _ in range(9)]
        boxTable = [ [set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = ord(board[i][j]) - ord('0')
                    if num not in rowTable[i]:
                        rowTable[i].add(num)
                    else:
                        return False
                    if num not in colTable[j]:
                        colTable[j].add(num)
                    else:
                        return False
                    if num not in boxTable[i // 3][j // 3]:
                        boxTable[i // 3][j // 3].add(num)
                    else:
                        return False
        return True