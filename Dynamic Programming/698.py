class Solution:
    def dfs(self, nums, k, target, cur):
        if cur == len(nums):
            return True
        for i in range(k):
            if target[i] >= nums[cur]:
                target[i] -= nums[cur]
                if self.dfs(nums, k, target, cur+1):
                    return True
                target[i] += nums[cur]
        return False
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        numsSum = sum(nums)
        if numsSum % k or k == 0:
            return False
        target = [(numsSum // k) for _ in range(k)]
        nums.sort(reverse=True)
        return self.dfs(nums, k, target, 0)