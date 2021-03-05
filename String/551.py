class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        prev_l = 0
        for i in range(len(s)):
            if s[i] == 'A':
                a += 1
                if a > 1:
                    return False
            if s[i] == 'L':
                if prev_l > 1:
                    return False
                else:
                    prev_l += 1
            else:
                prev_l = 0
        return True