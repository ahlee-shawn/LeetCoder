class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = max_num = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
            if dp[i] > max_num:
                max_num = dp[i]
        return max_num