class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        ans = 0
        for i in range(len(boxTypes)):
            if truckSize > boxTypes[i][0]:
                truckSize -= boxTypes[i][0]
                ans += (boxTypes[i][0] * boxTypes[i][1])
            else:
                ans += (truckSize * boxTypes[i][1])
                break
        return ans

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        for i in range(len(boxTypes)):
            if boxTypes[i][0] <= truckSize:
                ans += (boxTypes[i][0] * boxTypes[i][1])
                truckSize -= boxTypes[i][0]
            else:
                ans += (truckSize * boxTypes[i][1])
                break
            if truckSize == 0:
                break
        return ans