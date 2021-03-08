class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0
        i, j = 0, len(s)-1
    
        while True:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else: 
                return 2
            if i >= j:
                break
        return 1