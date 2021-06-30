class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for i in range(len(points)):
            value = points[i][0] ** 2 + points[i][1] ** 2
            heapq.heappush(pq, (value, i))
        ans = []
        for i in range(k):
            value, index = heapq.heappop(pq)
            ans.append([points[index][0], points[index][1]])
        return ans