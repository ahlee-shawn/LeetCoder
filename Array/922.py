class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if i % 2 == 0 and nums[i] %2 == 1:
                even.append(i)
            if i % 2 == 1 and nums[i] %2 == 0:
                odd.append(i)
        for i in range(len(even)):
            nums[even[i]], nums[odd[i]] = nums[odd[i]], nums[even[i]]
        return nums