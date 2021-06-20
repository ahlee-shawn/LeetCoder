class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        maxRight = [0 for _ in range(len(height))]
        maxValue = height[-1]
        for i in range(len(height)-1, -1, -1):
            maxRight[i] = maxValue
            maxValue = max(maxValue, height[i])
        answer, maxLeft = 0, 0
        for i in range(len(height)):
            maxLeft = max(maxLeft, height[i])
            tmp = (min(maxLeft, maxRight[i]) - height[i])
            if tmp > 0:
                answer += tmp
        return answer