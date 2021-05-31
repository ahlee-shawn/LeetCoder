class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                j = i + 1
                while j < len(nums) and nums[j] == 1:
                    j += 1
                ans = max(ans, j - i)
                i = j + 1
            else:
                i += 1
        return ans