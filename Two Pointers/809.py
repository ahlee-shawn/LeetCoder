class Solution:
    def compare(self, s, w):
        s_1 = s_2 = w_1 = w_2 = 0
        s_len, w_len = len(s), len(w)
        while s_1 < s_len and w_1 < w_len:
            if s[s_1] != w[w_1]:
                return 0
            s_2 = s_1 + 1
            while s_2 < s_len:
                if s[s_2] == s[s_1]:
                    s_2 += 1
                else:
                    break
            s_diff = s_2 - s_1
            w_2 = w_1 + 1
            while w_2 < w_len:
                if w[w_2] == w[w_1]:
                    w_2 += 1
                else:
                    break
            w_diff = w_2 - w_1  
            if s_diff == w_diff or (w_diff < s_diff and s_diff >= 3):
                s_1 = s_2
                w_1 = w_2  
            else:
                return 0
        if s_1 != s_len or w_1 != w_len:
            return 0
        return 1
        
    def expressiveWords(self, s: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            ans += self.compare(s, word)
        return ans