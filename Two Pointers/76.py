class Solution:
    def check_count(self, A, B):
        for i in range(26):
            if A[i] > B[i]:
                return False
        return True
        
    def minWindow(self, s: str, t: str) -> str:
        t_lower = [0 for _ in range(26)]
        t_upper = [0 for _ in range(26)]
        for i in range(len(t)):
            if 'a' <= t[i] <= 'z':
                t_lower[ord(t[i]) - ord('a')] += 1
            else:
                t_upper[ord(t[i]) - ord('A')] += 1
        ans_right = len(s)
        ans_left = 0
        left = right = 0
        window_lower = [0 for _ in range(26)]
        window_upper = [0 for _ in range(26)]
        avail = False
        while right < len(s):
            found = False
            # move right:
            while right < len(s):
                if 'a' <= s[right] <= 'z':
                    window_lower[ord(s[right]) - ord('a')] += 1
                else:
                    window_upper[ord(s[right]) - ord('A')] += 1
                right += 1
                lower = self.check_count(t_lower, window_lower)
                upper = self.check_count(t_upper, window_upper)
                if lower and upper:
                    found = True
                    break
            # move left:
            while left < right:
                if 'a' <= s[left] <= 'z':
                    window_lower[ord(s[left]) - ord('a')] -= 1
                else:
                    window_upper[ord(s[left]) - ord('A')] -= 1
                left += 1
                lower = self.check_count(t_lower, window_lower)
                upper = self.check_count(t_upper, window_upper)
                if not lower or not upper:
                    break
            if found and ans_right - ans_left > right - left:
                ans_right = right
                ans_left = left - 1
                avail = True
        if avail:
            return s[ans_left:ans_right]
        else:
            return ""