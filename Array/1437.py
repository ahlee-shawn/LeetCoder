class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        prev_one = -2*k
        for i in range(len(nums)):
            if nums[i] == 1:
                if i-prev_one-1 < k:
                    return False
                prev_one = i
        return True