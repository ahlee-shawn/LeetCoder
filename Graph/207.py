class Solution:
    def isCycle(self, current, visited, graph):
        # if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then there is a ring
        if visited[current] == -1:
            return True
        if visited[current] == 1:
            return False
        visited[current] = -1
        for neighbor in graph[current]:
            if self.isCycle(neighbor, visited, graph) == True:
                return True
        # if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors
        visited[current] = 1
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if node v has not been visited, then mark it as 0
        visited = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            graph[i].append(j)
        for i in range(numCourses):
            if self.isCycle(i, visited, graph) == True:
                return False
        return True