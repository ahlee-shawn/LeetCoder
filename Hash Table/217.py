class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = set()
        for i in range(len(nums)):
            if nums[i] in table:
                return True
            else:
                table.add(nums[i])
        return False