class Solution:
    def search_start_index(self, nums, target):
        index = -1
        start, end = 0, len(nums)-1
        while start <= end:
            mid_point = (start + end) // 2
            if nums[mid_point] >= target:
                end = mid_point - 1
            else:
                start = mid_point + 1
            if nums[mid_point] == target:
                index = mid_point
        return index
    
    def search_end_index(self, nums, target):
        index = -1
        start, end = 0, len(nums)-1
        while start <= end:
            mid_point = (start + end) // 2
            if nums[mid_point] > target:
                end = mid_point - 1
            else:
                start = mid_point + 1
            if nums[mid_point] == target:
                index = mid_point
        return index
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_index = self.search_start_index(nums, target)
        end_index = self.search_end_index(nums, target)
        return [start_index, end_index]