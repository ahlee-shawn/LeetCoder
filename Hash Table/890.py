class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            w2p = {} # wordToPattern Dictionary
            p2w = {} # patternToWord Dictionary
            match = True
            for i in range(len(word)):
                if word[i] not in w2p:
                    w2p[word[i]] = pattern[i]
                elif w2p[word[i]] != pattern[i]:
                    match = False
                    break
                if pattern[i] not in p2w:
                    p2w[pattern[i]] = word[i]
                elif p2w[pattern[i]] != word[i]:
                    match = False
                    break
            if match:
                ans.append(word)
        return ans