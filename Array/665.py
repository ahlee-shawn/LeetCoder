class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        temp = nums[1] < nums[0]
        for i in range(2, len(nums)):
            if nums[i-1] > nums[i]:
                if nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
                if temp:
                    return False
                temp = True
        return True