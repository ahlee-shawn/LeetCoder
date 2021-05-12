class Solution:
    def bfs(self, isConnected, visited, queue):
        while queue:
            curNode = queue.popleft()
            visited[curNode] = True
            for i in range(len(isConnected)):
                if isConnected[curNode][i] and not visited[i]:
                    queue.append(i)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False for _ in range(len(isConnected))]
        ans = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                ans += 1
                queue = deque()
                queue.append(i)
                self.bfs(isConnected, visited, queue)
        return ans