class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        dp = [0 for _ in range(len(nums))]
        count = 0
        val = 0
        increment = 0
        for i in range(len(nums)):
            if nums[i] > right:
                dp[i] = 0
                count = 0
                val = 0
                increment = 0
            elif nums[i] < left:
                val += 1
                dp[i] = count + increment
            else:
                count += 1
                increment = val
                dp[i] = count + increment
        # print(dp)
        return sum(dp)