class Solution:
    def dfs(self, avail_nums, partial_permutation, ans):
        if not avail_nums:
            ans.append(partial_permutation)
            return ans
        else:
            used_num = set()
            for i in range(len(avail_nums)):
                if avail_nums[i] not in used_num:
                    new_avail_nums = avail_nums.copy()
                    new_avail_nums.pop(i)
                    new_partial_permutation = partial_permutation.copy()
                    new_partial_permutation.append(avail_nums[i])
                    ans = self.dfs(new_avail_nums, new_partial_permutation, ans)
                    used_num.add(avail_nums[i])
        return ans
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.dfs(nums, [], [])