class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = dict()
        for i in range(len(s)):
            if s[i] not in table:
                table[s[i]] = [i, 1]
            else:
                table[s[i]][1] += 1
        ans = float('inf')
        for key in table:
            if table[key][1] == 1 and table[key][0] < ans:
                ans = table[key][0]
        if ans == float('inf'):
            return -1
        else:
            return ans