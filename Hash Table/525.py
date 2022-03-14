class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table = dict()
        table[0] = -1
        result = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count not in table:
                table[count] = i
            else:
                if i - table[count] > result:
                    result = i - table[count]
        return result