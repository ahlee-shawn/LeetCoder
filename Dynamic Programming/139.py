# TLE
class Solution:
    def isSuffix(self, s, word, i):
        for j in len(word):
            if s[i+j] != word[j]:
                return False
        return True

    def dfs(self, s, wordDict, i):
        if i == len(s):
            return True
        returnValue = False
        for word in wordDict:
            # compare word and s starting from i
            if self.isSuffix(s, word, i):
                returnValue = returnValue or self.dfs(s, wordDict, i+len(word))
                if returnValue:
                    return True
        return returnValue

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs(s, wordDict, 0)
