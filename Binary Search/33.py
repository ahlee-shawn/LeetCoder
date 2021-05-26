class Solution:
    def helper(self, nums, start, end, target):
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if start >= end:
            return -1
        if nums[mid] > nums[start]:
            if nums[start] < target < nums[mid]:
                return self.helper(nums, start, mid-1, target)
            else:
                return self.helper(nums, mid+1, end, target)
        else:
            if nums[mid] < target < nums[end]:
                return self.helper(nums, mid+1, end, target)
            else:
                return self.helper(nums, start, mid-1, target)
        
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, len(nums)-1, target)