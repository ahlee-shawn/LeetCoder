import random

class Solution:

    def __init__(self, w: List[int]):
        self.weight = [w[0]]
        for i in range(1, len(w)):
            self.weight.append(self.weight[-1]+w[i])
        
    def binarySearch(self, target):
        start, end = 0, len(self.weight)-1
        if self.weight[start] >= target:
            return start
        if self.weight[end] == target:
            return end
        while start+1 < end:
            mid = start + ((end-start) // 2)
            if self.weight[mid] == target:
                return mid
            if self.weight[mid] > target:
                end = mid
            if self.weight[mid] < target:
                start = mid
        if self.weight[start] >= target:
            return start
        else:
            return end

    def pickIndex(self) -> int:
        target = random.randint(1, self.weight[-1])
        index = self.binarySearch(target)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()