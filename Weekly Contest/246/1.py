# Largest Odd Number in String
class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        cur = ""
        for i in range(len(num)):
            cur += num[i]
            if int(num[i]) % 2:
                ans = cur
        return ans