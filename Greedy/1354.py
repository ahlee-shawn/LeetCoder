class Solution:
    def isPossible(self, target: List[int]) -> bool:
        arrSum = -sum(target)
        A = [-a for a in target]
        heapq.heapify(A)
        while True:
            maxValue = heapq.heappop(A)
            arrSum -= maxValue
            if maxValue == -1 or arrSum == -1:
                return True
            elif maxValue > arrSum or arrSum == 0 or maxValue % arrSum == 0:
                return False
            maxValue %= arrSum
            arrSum += maxValue
            heapq.heappush(A, maxValue)