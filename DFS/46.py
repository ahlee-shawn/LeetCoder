# Package
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)

# DFS
class Solution:
    def dfs(self, avail_nums, partial_permutation, ans):
        if not avail_nums:
            ans.append(partial_permutation)
            return ans
        else:
            for i in range(len(avail_nums)):
                new_avail_nums = avail_nums.copy()
                new_avail_nums.pop(i)
                new_partial_permutation = partial_permutation.copy()
                new_partial_permutation.append(avail_nums[i])
                ans = self.dfs(new_avail_nums, new_partial_permutation, ans)
        return ans
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.dfs(nums, [], [])