class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2:
            return False
        nums.sort()
        target = totalSum / 2
        table = set()
        table.add(0)
        for num in nums:
            newElement = []
            for element in table:
                newElement.append(element+num)
            for element in newElement:
                table.add(element)
            if target in table:
                return True
        return False