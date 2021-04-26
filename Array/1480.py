class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            ans[i] += (nums[i] + prev)
            prev += nums[i]
        return ans