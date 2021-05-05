# Backtracking -> Time Exceeded
class Solution:
    def jumpLast(self, nums, visited, currentIndex):
        if currentIndex >= len(nums)-1:
            return True
        visited[currentIndex] = True
        for i in range(nums[currentIndex], 0, -1):
            if not visited[currentIndex+i]:
                if self.jumpLast(nums, visited, currentIndex+i):
                    return True
        return False
    
    def canJump(self, nums: List[int]) -> bool:
        visited = [False for _ in range(len(nums))]
        return self.jumpLast(nums, visited, 0)

# Greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0