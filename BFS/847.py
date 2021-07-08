class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target_status = (1 << n) - 1
        queue = deque()
        visited = [set() for _ in range(n)]
        for i in range(n):
            queue.append((0, i, 1 << i)) #distance, node, status
        while queue:
            (cur_distance, cur_node, cur_status) = queue.popleft()
            if cur_status == target_status:
                return cur_distance
            for next_node in graph[cur_node]:
                next_status = cur_status | (1 << next_node)
                if next_status not in visited[next_node]:
                    visited[next_node].add(next_status)
                    queue.append((cur_distance + 1, next_node, next_status))
        return -1