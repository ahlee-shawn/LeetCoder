class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = Counter(nums)
        return heapq.nlargest(k, table.keys(), key=table.get)