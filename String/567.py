class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        table = [0 for _ in range(26)]
        window = [0 for _ in range(26)]
        for i in range(len(s1)):
            table[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        if table == window:
            return True
        start = 0
        for i in range(len(s1), len(s2)):
            window[ord(s2[start]) - ord('a')] -= 1
            window[ord(s2[i]) - ord('a')] += 1
            if table == window:
                return True
            start += 1
        return False