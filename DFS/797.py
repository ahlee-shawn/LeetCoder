class Solution:
    def dfs(self, graph, current_node, current_path, all_paths):
        if current_node == len(graph)-1:
            all_paths.append(current_path)
            return all_paths
        else:
            for i in range(len(graph[current_node])):
                new_path = current_path.copy()
                new_path.append(graph[current_node][i])
                all_paths = self.dfs(graph, graph[current_node][i], new_path, all_paths)
            return all_paths
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.dfs(graph, 0, [0], [])