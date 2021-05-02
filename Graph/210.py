class Solution:
    def topologicalSort(self, current, visited, graph, ans):
        if visited[current] == -1:
            return False
        if visited[current] == 1:
            return True
        visited[current] = -1
        for neighbor in graph[current]:
            if self.topologicalSort(neighbor, visited, graph, ans) == False:
                return False
        ans.append(current)
        visited[current] = 1
        return True
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        visited = [0 for _ in range(numCourses)]
        graph = [[] for  _ in range(numCourses)]
        for j, i in prerequisites:
            graph[i].append(j)
        for i in range(numCourses):
            if self.topologicalSort(i, visited, graph, ans) == False:
                return []
        return ans[::-1]