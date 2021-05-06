class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = dict()
        table[0] = 1
        preSum = ans = 0
        for num in nums:
            preSum += num
            if preSum - k in table:
                ans += table[preSum-k]
            if preSum not in table:
                table[preSum] = 1
            else:
                table[preSum] += 1
        return ans