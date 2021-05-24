class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if ord('A') <= ord(s[i]) <= ord('Z'):
                s[i] = chr(ord(s[i]) - ord('A') + ord('a'))
        return ''.join(s)