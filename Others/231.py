class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        binary_n = bin(n)
        for i in range(3, len(binary_n)):
            if binary_n[i] == '1':
                return False
        return True