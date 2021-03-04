class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            temp = 0
            for j in range(len(accounts[0])):
                temp += accounts[i][j]
            if temp > max_wealth:
                max_wealth = temp
        return max_wealth