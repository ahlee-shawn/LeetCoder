class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = bin(x), bin(y)
        if len(x) < len(y):
            x, y = y, x
        ans = 0
        for i in range(1, len(y)-1):
            ans += int(x[-i] != y[-i])
        if len(x) != len(y):
            for i in range(len(y)-1, len(x)-1):
                ans += int(x[-i] == '1')
        return ans

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')