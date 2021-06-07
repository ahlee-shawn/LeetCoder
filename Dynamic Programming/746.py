class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i_1 = cost[1]
        i_2 = cost[0]
        for i in range(2, len(cost)):
            temp = i_1
            i_1 = min(i_1, i_2) + cost[i]
            i_2 = temp
        return min(i_1, i_2)