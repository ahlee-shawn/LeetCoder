class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        correct_sum = n*(n+1)/2
        nums_sum = sum(nums)
        numbers = set()
        for i in nums:
            if i in numbers:
                ans.append(i)
                ans.append(int(correct_sum - nums_sum+i))
                return ans
            else:
                numbers.add(i)