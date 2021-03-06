import numpy as np
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alphabet = np.zeros(26, dtype=int)
        for i in range(len(s)):
            alphabet[ord(s[i])-ord('a')] += 1
        for i in range(len(t)):
            alphabet[ord(t[i])-ord('a')] -= 1
            if alphabet[ord(t[i])-ord('a')] == -1:
                return t[i]