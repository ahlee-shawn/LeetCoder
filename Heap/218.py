class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        
        points  = [(l,h,-1,i) for i, (l,r,h) in enumerate(buildings)]
        points += [(r,h,1,i) for i, (l,r,h) in enumerate(buildings)]
        points.sort(key = lambda x: (x[0], x[1]*x[2]))
        
        heap = [(0, -1)]
        active = set([-1])
        
        
        for (x, h, lr, index) in points:
            if lr == -1:
                active.add(index)
            elif lr == 1:
                active.remove(index)
                
            if lr == -1:
                if h > -heap[0][0]:
                    ans.append([x, h])
                heappush(heap, (-h, index))
            else:
                while heap and heap[0][1] not in active:
                    heappop(heap)
                if -heap[0][0] != ans[-1][1]: 
                    ans.append([x, -heap[0][0]])
                
        return ans