class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0 for _ in range(len(nums))]
        preSum = 0
        for i in range(len(nums)):
            self.arr[i] += (preSum + nums[i])
            preSum += nums[i]     
        print(self.arr)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.arr[right]
        else:
            return self.arr[right] - self.arr[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)