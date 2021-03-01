class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        visited = [False for _ in range(n)]
        sequence = set()
        
        def DFS(s):
            sequence.add(s)
            if len(s) == n:
                return
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    DFS(s+tiles[i])
                    visited[i] = False
        DFS("")
        return len(sequence) - 1