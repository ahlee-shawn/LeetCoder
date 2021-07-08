class Solution:
        
    def consecutiveNumbersSum(self, n: int) -> int:
        if n == 1:
            return 1
        ans = 0
        upper_bound = (-1 + int(sqrt(1 + 8*n))) // 2
        for i in range(1, upper_bound + 1):
            tmp = (i * (i - 1)) / 2
            if (n - tmp) % i == 0:
                if ((n - tmp) / i) >= 1:
                    ans += 1
        return ans