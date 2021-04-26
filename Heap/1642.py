class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        difference_heap = []
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heapq.heappush(difference_heap, diff)
            if len(difference_heap) > ladders:
                bricks -= heapq.heappop(difference_heap)
            if bricks < 0:
                return i
        return len(heights) - 1