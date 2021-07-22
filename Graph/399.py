class Solution:
    def findPath(self, table, start, end):
        queue = deque()
        queue.append([start, 1])
        visited = set()
        visited.add(start)
        while queue:
            curNode, value = queue.popleft()
            if curNode == end:
                return value
            for key in table[curNode]:
                if key not in visited:
                    visited.add(key)
                    queue.append([key, value * table[curNode][key]])
        return -1.0
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        table = {}
        for i in range(len(equations)):
            start = equations[i][0]
            end = equations[i][1]
            value = values[i]
            if start not in table:
                table[start] = {}
            if end not in table:
                table[end] = {}
            table[start][end] = value
            table[end][start] = 1 / value
        ans = []
        for query in queries:
            start = query[0]
            end = query[1]
            if start in table:
                ans.append(self.findPath(table, start, end))
            else:
                ans.append(-1)
        return ans