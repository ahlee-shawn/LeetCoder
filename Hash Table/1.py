class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        table[target - nums[0]] = 0
        for i in range(1, len(nums)):
            if table.get(nums[i]) is None:
                table[target - nums[i]] = i
            else:
                return [i, table.get(nums[i])]