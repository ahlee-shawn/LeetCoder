class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        i = 1
        while True:
            if n < 0:
                break
            ans += 1
            n -= i
            i += 1
        return ans-1