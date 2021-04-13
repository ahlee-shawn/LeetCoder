class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        i = 0
        while True:
            try:
                c = strs[0][i]
                for j in range(1, len(strs)):
                    if strs[j][i] != c:
                        return ans
                ans += c
                i += 1
            except:
                return ans