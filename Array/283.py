class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[swap_index] = nums[i]
                swap_index += 1
        for i in range(swap_index, len(nums)):
            nums[i] = 0