class Solution:
    def help(self, nums, start, end):
        last, now = 0, 0
        for i in range(start, end):
            last, now = now, max(last+nums[i], now)
        return now
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # if len(nums) == 2:
        #     return 0
        withoutFirst = self.help(nums, 1, len(nums))
        withoutLast = self.help(nums, 0, len(nums)-1)
        return max(withoutFirst, withoutLast)