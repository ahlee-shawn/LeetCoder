class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = [0 for _ in range(26)]
        tCount = [0 for _ in range(26)]
        for i in range(len(s)):
            sCount[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            tCount[ord(t[i]) - ord('a')] += 1
        for i in range(26):
            if sCount[i] != tCount[i]:
                return False
        return True