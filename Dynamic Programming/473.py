# Dynamic Programming

# DFS Revised
class Solution:
    def dfs(self, matchsticks, target, cur):
        if cur == len(matchsticks):
            return True
        for i in range(4):
            if target[i] >= matchsticks[cur]:
                target[i] -= matchsticks[cur]
                if self.dfs(matchsticks, target, cur+1):
                    return True
                target[i] += matchsticks[cur]
        return False
        
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticksSum = sum(matchsticks)
        if matchsticksSum % 4:
            return False
        target = [(matchsticksSum // 4) for _ in range(4)]
        matchsticks.sort(reverse=True)
        return self.dfs(matchsticks, target, 0)

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