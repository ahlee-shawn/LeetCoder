class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = []
        for i in range(int(sqrt(c))+1):
            squares.append(i**2)
        table = set()
        for square in squares:
            table.add(c-square)
            if square in table:
                return True
        return False