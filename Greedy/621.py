# Math
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table = [0 for _ in range(26)]
        for task in tasks:
            table[ord(task)-ord('A')] += 1
        maxCount, maxIndexCount = 0, 0
        for i in range(26):
            if table[i] > maxCount:
                maxCount = table[i]
                maxIndexCount = 1
            elif table[i] == maxCount:
                maxIndexCount += 1
        partition = maxCount - 1
        slotPerPartition = n - (maxIndexCount - 1)
        slots = partition * slotPerPartition
        emptySlots = max(0, slots - (len(tasks) - maxCount*maxIndexCount))
        return len(tasks) + emptySlots

# len(tasks) = m
# Unique Tasks: k
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table = {}
        for task in tasks: # O(m)
            if task not in table:
                table[task] = 1
            else:
                table[task] += 1
        pq = []
        for key in table: # O(k)
            pq.append((-table[key], key))
        heapq.heapify(pq) # O(k)
        taskQueue = deque()
        lastExecute = {}
        time = 0
        while pq: #O(m)
            for i in range(n+1): #O((n+1)*logk)
                if pq:
                    taskQueue.append(heapq.heappop(pq))
            while taskQueue: # O(n+1)
                time += 1
                curTaskLeft, curTaskName = taskQueue.popleft()
                if curTaskName in lastExecute:
                    time += max(0, n+1+lastExecute[curTaskName]-time)
                lastExecute[curTaskName] = time
                if curTaskLeft < -1:
                    heapq.heappush(pq, (curTaskLeft+1, curTaskName))
        return time

# Time: O(m + 2k + m*((n+1)(logk+1))) = O(mnlogK)
# Space: O(k)