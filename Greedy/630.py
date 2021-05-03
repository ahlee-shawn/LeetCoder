import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key = lambda x: (x[1], x[0]))
        priory_queue = []
        day = 0
        for i in range(len(courses)):
            if day + courses[i][0] <= courses[i][1]:
                heapq.heappush(priory_queue, courses[i][0]*-1)
                day += courses[i][0]
            else:
                if priory_queue and priory_queue[0] < courses[i][0]*-1:
                    day = day - priory_queue[0]*-1 + courses[i][0]
                    heapq.heappop(priory_queue)
                    heapq.heappush(priory_queue, courses[i][0]*-1)
        return len(priory_queue)