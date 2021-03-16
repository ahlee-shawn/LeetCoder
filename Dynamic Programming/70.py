class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0]*(n+1)
        def dp(target):
            if table[target] != 0:
            if target == 1:
                return 1
            elif target == 2:
                return 2
            else:
                temp = dp(target-1) + dp(target-2)
                table[target] = temp
                return temp
        return dp(n)