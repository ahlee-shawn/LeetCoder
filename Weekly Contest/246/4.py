# Minimum Absolute Difference Queries
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        count = [[0 for _ in range(101)] for _ in range(len(nums))]
        for i in range(len(nums)):
            count[i][nums[i]] += 1
        for i in range(1, len(nums)):
            for j in range(101):
                count[i][j] += count[i-1][j]
        for query in queries:
            if query[0]:
                start = count[query[0]-1]
            else:
                start = [0] * 101
            end = count[query[1]]
            diff = [end[i] - start[i] for i in range(101)]
            last = -1
            minValue = float('inf')
            for i in range(101):
                if diff[i]:
                    if last != -1:
                        minValue = min(minValue, i-last)
                        if minValue == 1:
                            break
                    last = i
            if diff[last] == query[1] - query[0] + 1:
                minValue = -1
            ans.append(minValue)
        return ans