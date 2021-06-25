class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            forward[i] = forward[i-1] * nums[i-1]
        backward = [1 for _ in range(len(nums))]
        index = len(nums) - 1
        for i in range(1, len(nums)):
            backward[i] = backward[i-1] * nums[index]
            index -= 1
        ans = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            ans[i] *= (forward[i] * backward[len(backward)-1 -i])
        return ans