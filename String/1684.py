class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed_set = set()
        for i in range(len(allowed)):
            allowed_set.add(allowed[i])
        for i in range(len(words)):
            temp = 1
            for j in range(len(words[i])):
                if words[i][j] not in allowed_set:
                    temp = 0
                    break
            ans += temp
        return ans