class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] < dp[0]:
                dp[0] = nums[i]
            elif nums[i] > dp[-1]:
                dp.append(nums[i])
            elif dp[0] < nums[i] < dp[-1]:
                for j in range(1, len(dp)):
                    if dp[j] > nums[i]:
                        dp[j] = nums[i]
            if len(dp) == 3:
                return True
        return False