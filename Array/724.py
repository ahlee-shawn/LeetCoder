class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            total_sum += num
        left = 0
        right = total_sum
        for i in range(len(nums)):
            num = nums[i]
            right -= num
            if left == right:
                return i
            left += num
        return -1