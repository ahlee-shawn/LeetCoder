class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_table = dict()
        s_table = dict()
        string = s.split()
        if len(pattern) != len(string):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in pattern_table:
                pattern_table[pattern[i]] = string[i]
            else:
                if pattern_table[pattern[i]] != string[i]:
                    return False
            if string[i] not in s_table:
                s_table[string[i]] = pattern[i]
            else:
                if s_table[string[i]] != pattern[i]:
                    return False
        
        return True