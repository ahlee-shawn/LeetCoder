class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table_s = dict()
        table_t = dict()
        for i in range(len(s)):
            if s[i] not in table_s:
                table_s[s[i]] = t[i]
            else:
                if table_s[s[i]] != t[i]:
                    return False
            if t[i] not in table_t:
                table_t[t[i]] = s[i]
            else:
                if table_t[t[i]] != s[i]:
                    return False
        return True