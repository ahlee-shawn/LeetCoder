class Solution:
    def helper(self, s, left, right):
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
        
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            length1 = self.helper(s, i, i)
            length2 = self.helper(s, i, i+1)
            length = max(length1, length2)
            if length > end - start:
                end = i + (length // 2)
                start = i - ((length-1) // 2)
        return s[start:end+1]