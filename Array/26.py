class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = len(nums)
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                ans -= 1
                nums.pop(i)
        return ans