class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        table = {}
        start = 0
        for i in range(len(s)):
            if s[i] in table:
                start = max(start, table[s[i]]+1)
            ans = max(ans, i-start+1)
            table[s[i]] = i
        return ans