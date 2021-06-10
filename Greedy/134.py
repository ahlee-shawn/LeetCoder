# O(N)
# https://leetcode.com/problems/gas-station/discuss/128187/O(n)-time-and-O(1)-space-python-solution-with-new-idea-and-explanation
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        diff = [x-y for x, y in zip(gas, cost)]
        minVal = diff[0]
        index = 0
        cummulatedSum = diff[0]
        for i in range(1, len(diff)):
            cummulatedSum += diff[i]
            if cummulatedSum < minVal:
                minVal = cummulatedSum
                index = i
        return (index + 1) % len(cost)

# O(N^2)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            valid = True
            gasRemain = gas[i]
            for j in range(n):
                if cost[(i+j)%n] > gasRemain:
                    valid = False
                    break
                else:
                    gasRemain -= cost[(i+j)%n]
                    gasRemain += gas[(i+j+1)%n]
            if valid:
                return i
        return -1