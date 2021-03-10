class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        for i in [1024,6561,15625]:
            while True:
                if n % i == 0:
                    n /= i
                else:
                    break
        for i in [2,3,5]:
            while True:
                if n % i == 0:
                    n /= i
                else:
                    break
        if n == 1:
            return True
        else:
            return False