# Time: NlogN
# Space: N
class Solution:
	def findUnsortedSubarray(self, nums: List[int]) -> int:
		start, end = -1, -1
		nums_sorted = sorted(nums)
		for i in range(len(nums)):
			if nums_sorted[i] != nums[i]:
				if start == -1:
					start = i
				else:
					end = i
		if start == end:
			return 0
		else:
			return end - start + 1