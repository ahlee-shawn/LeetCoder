# Union Find
class Solution:
    def __init__(self):
        self.table = [i for i in range(26)]
    
    def findOrigin(self, index):
        while self.table[index] != index:
            index = self.table[index]
        return index
    
    def equationsPossible(self, equations: List[str]) -> bool:
        for equation in equations:
            if equation[1] == "=":
                left = ord(equation[0]) - ord('a')
                right = ord(equation[3]) - ord('a')
                if left > right:
                    left, right = right, left
                leftOrigin = self.findOrigin(left)
                rightOrigin = self.findOrigin(right)
                if leftOrigin != rightOrigin:
                    self.table[rightOrigin] = leftOrigin
        for equation in equations:
            if equation[1] == "!":
                left = ord(equation[0]) - ord('a')
                right = ord(equation[3]) - ord('a')
                if left > right:
                    left, right = right, left
                leftOrigin = self.findOrigin(left)
                rightOrigin = self.findOrigin(right)
                if leftOrigin == rightOrigin:
                    return False
        return True