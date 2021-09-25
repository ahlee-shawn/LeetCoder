class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        table = dict()
        for num in nums:
            if num not in table:
                table[num] = 1
            else:
                table[num] += 1
        ans = 0
        for num in table:
            count = table[num]
            if count > 1:
                ans += (count * (count-1) // 2)
        return ans