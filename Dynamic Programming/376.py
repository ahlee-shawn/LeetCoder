class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        ans = 0
        pre_dif = float("inf")
        for i in range(1, len(nums)):
            cur_dif = nums[i] - nums[i-1]
            #print(nums[i], nums[i-1], cur_dif, pre_dif)
            if pre_dif != float("inf") and cur_dif*pre_dif < 0:
                ans += 1
            if cur_dif != 0:
                pre_dif = cur_dif
                
        if pre_dif != float("inf"):
            return ans+2
        else:
            return 1