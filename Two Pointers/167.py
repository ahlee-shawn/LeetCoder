class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small, big = 0, len(numbers)-1
        while small < big:
            temp = numbers[small] + numbers[big]
            if temp == target:
                return [small+1, big+1]
            elif temp > target:
                big -= 1
            else:
                small += 1