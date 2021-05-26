class Solution:
    def minPartitions(self, n: str) -> int:
        ans = '0'
        for c in n:
            if c > ans:
                ans = c
        return int(ans)