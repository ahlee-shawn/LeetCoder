class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n >= 729:
            if n % 729 == 0:
                return self.isPowerOfThree(n // 729)
            else:
                return False
        else:
            if n % 3 == 0:
                return self.isPowerOfThree(n // 3)
            else:
                return False