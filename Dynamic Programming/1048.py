class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))
        newTable = {}
        length = i = ans = 0
        while i < len(words): 
            if len(words[i]) == length:
                newCount = 1
                if len(words[i]) != 1:
                    for j in range(len(words[i])):
                        key = words[i][:j] + words[i][j+1:]
                        print('key', key)
                        newCount = max(table.get(key, 0)+1, newCount)
                newTable[words[i]] = newCount
                i += 1
            else:
                length = len(words[i])
                table = newTable
                newTable = {}
            if newTable:
                ans = max(ans, max(newTable.values()))
        return ans