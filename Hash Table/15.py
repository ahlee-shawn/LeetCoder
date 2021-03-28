class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            table = set()
            target = 0 - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] in table:
                    ans.add((nums[i], 0-nums[i]-nums[j], nums[j]))
                else:
                    table.add(target - nums[j])
        return list(ans)