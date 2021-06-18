class NumArray:

    def __init__(self, nums: List[int]):
        self.cummulate = [0 for _ in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            self.cummulate[i] += (self.cummulate[i-1] + nums[i-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.cummulate[right+1] - self.cummulate[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)