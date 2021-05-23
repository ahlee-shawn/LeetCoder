class Solution:
    def findMaxDiff(self, n, Arr):
        Arr.sort()
        maxDiff = Arr[0]
        for i in range(len(Arr)-1):
            maxDiff = max(maxDiff, Arr[i+1] - Arr[i])
        return max(maxDiff, n - Arr[-1])
        
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxH = self.findMaxDiff(h, horizontalCuts)
        maxW = self.findMaxDiff(w, verticalCuts)
        return (maxH * maxW) % (10**9+7)