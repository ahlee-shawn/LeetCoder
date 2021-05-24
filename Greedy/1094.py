class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pq = []
        for trip in trips:
            heapq.heappush(pq, (trip[1], trip[0]))
            heapq.heappush(pq, (trip[2], -trip[0]))
        used = 0
        while pq:
            used += heapq.heappop(pq)[1]
            if used > capacity:
                return False
        return True