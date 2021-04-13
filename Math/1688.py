import math
class Solution:
    def recursion(self, n):
        if n == 1:
            return 0
        return self.recursion(int(n/2)) + math.ceil(n/2)
    def numberOfMatches(self, n: int) -> int:
        return self.recursion(n)

'''
Life hacker
'''
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1