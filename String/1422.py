class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
        left_zeros = int(s[0] == '0')
        right_ones = ones - int(s[0] == '1')
        ans = left_zeros + right_ones
        for i in range(2, len(s)):
            if s[i-1] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            ans = max(ans, left_zeros+right_ones)
        return ans