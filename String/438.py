class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        table = [0 for _ in range(26)]
        window = [0 for _ in range(26)]
        for i in range(len(p)):
            table[ord(p[i]) - ord('a')] += 1
            window[ord(s[i]) - ord('a')] += 1
        start = 0
        ans = []
        if table == window:
            ans.append(start)
        for i in range(len(p), len(s)):
            window[ord(s[start]) - ord('a')] -= 1
            window[ord(s[i]) - ord('a')] += 1
            start += 1
            if table == window:
                ans.append(start)
        return ans