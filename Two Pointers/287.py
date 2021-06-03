class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[nums[0]], nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow