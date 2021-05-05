# BFS
class Solution:
    def jump(self, nums: List[int]) -> int:
        table = set()
        table.add(0)
        jump = 0
        while len(nums)-1 not in table:
            jump += 1
            for index in list(table):
                for i in range(nums[index]+1):
                    table.add(index+i)
        return jump

# Greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        current_max = last_max = jump = i = 0
        while current_max < len(nums)-1:
            while i <= last_max:
                current_max = max(i+nums[i], current_max)
                i += 1
            last_max = current_max
            jump += 1
        return jump