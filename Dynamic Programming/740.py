class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        table = dict()
        for num in nums:
            if num not in table:
                table[num] = 1
            else:
                 table[num] += 1
        used = passed = 0
        for key in sorted(table):
            if key - 1 in table:
                used, passed = passed + key * table[key], max(used, passed)
            else:
                used, passed = max(used, passed) + key * table[key], max(used, passed)
        return max(used, passed)