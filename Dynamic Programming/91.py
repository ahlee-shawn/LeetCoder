class Solution:
    def __init__(self):
        self.table = {}

    def dfs(self, s, index):
        if index == len(s):
            self.table[index] = 1
        else:
            hop_once = hop_twice = 0
            # 1-hop:
            partial_string = s[index]
            if "1" <= partial_string <= "9":
                if (index + 1) not in self.table:
                    self.dfs(s, index+1)
                hop_once = self.table[(index + 1)]
            # 2-hop:
            if index < len(s) - 1:
                partial_string += s[index+1]
                if "10" <= partial_string <= "26":
                    if (index + 2) not in self.table:
                        self.dfs(s, index+2)
                    hop_twice = self.table[(index + 2)]
            self.table[index] = hop_once + hop_twice
            
    def numDecodings(self, s: str) -> int:
        self.dfs(s, 0)
        return self.table[0]
# TLE
class Solution:
    def __init__(self):
        self.table = {}
        self.ans = 0

    def dfs(self, s, index):
        if index == len(s):
            self.ans += 1
        else:
            # step1: 1
            partial_string = s[index]
            if "1" <= partial_string <= "9":
                self.dfs(s, index + 1)
            # step2: 12
            if index < len(s)-1:
                partial_string += s[index+1]
                if "10" <= partial_string <= "26":
                    self.dfs(s, index + 2)


    def numDecodings(self, s: str) -> int:
        self.dfs(s, 0)
        return self.ans