# Recurrsion -> Time Exceeded

class Solution:
    def findLIS(self, nums, maxLength, end):
        for i in range(end):
            self.findLIS(nums, maxLength, i)
            if nums[end] > nums[i]:
                maxLength[end] = max(maxLength[end], maxLength[i]+1)
        return maxLength[end]
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLength = [1 for _ in range(len(nums))]
        self.findLIS(nums, maxLength, len(nums)-1)
        print(maxLength)
        return max(maxLength)

# Recurrsion Optimized
class Solution:
    def findLIS(self, nums, visited, maxLength, end):
        if not visited[end]:
            for i in range(end):
                self.findLIS(nums, visited, maxLength, i)
                if nums[end] > nums[i]:
                    maxLength[end] = max(maxLength[end], maxLength[i]+1)
            visited[end] = True
        return maxLength[end]
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        visited = [False for _ in range(len(nums))]
        maxLength = [1 for _ in range(len(nums))]
        self.findLIS(nums, visited, maxLength, len(nums)-1)
        print(maxLength)
        return max(maxLength)


# Patience Sort
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLengthIndex = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] < maxLengthIndex[0]:
                maxLengthIndex[0] = nums[i]
            elif nums[i] > maxLengthIndex[-1]:
                maxLengthIndex.append(nums[i])
            else:
                if len(maxLengthIndex) >= 3:
                    for j in range(len(maxLengthIndex)-1):
                        if maxLengthIndex[j] < nums[i] < maxLengthIndex[j+1]:
                            maxLengthIndex[j+1] = nums[i]
                else:
                    if maxLengthIndex[0] < nums[i] < maxLengthIndex[-1]:
                            maxLengthIndex[-1] = nums[i]
        return len(maxLengthIndex)