# Dynamic Programming


# DFS: Too Slow
class Solution:
    def __init__(self):
        self.length = [0, 0, 0, 0]
        
    def dfs(self, matchsticks, cur):
        print(cur)
        if cur == len(matchsticks):
            if self.length[0] == self.length[1] == self.length[2] == self.length[3]:
                return True
            else:
                return False
        else:
            for i in range(4):
                self.length[i] += matchsticks[cur]
                if self.dfs(matchsticks, cur+1):
                    return True
                self.length[i] -= matchsticks[cur]
            return False
        
    def makesquare(self, matchsticks: List[int]) -> bool:
        return self.dfs(matchsticks, 0)