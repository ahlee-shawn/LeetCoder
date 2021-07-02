# TLE
class Solution:
    def check_relation(self, a, b):
        difference = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                difference +=1
                if difference >= 2:
                    return 0
        if difference == 1:
            return 1
        else: 
            return 0
  
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        start = -1
        for i in range(len(wordList)):
            if wordList[i] == beginWord:
                start = i
                break
                
        if start == -1:
            wordList.append(beginWord)
            start = len(wordList) - 1
        
        target = -1 # store the index of endWord in the graph
        # Create Graph
        n = len(wordList) # 4
        graph = [[0 for _ in range(n)] for _ in range(n)] # Space: O(n^2)
        for i in range(n): # Time: O(n^2)
            if wordList[i] == endWord:
                target = i #2
            for j in range(i+1, n):
                reachable = self.check_relation(wordList[i], wordList[j])
                graph[i][j] = reachable
                graph[j][i] = reachable
                
        if target == -1:
            return 0

        #BFS
        queue = deque()
        queue.append([start])
        hop = 0
        while queue: # Time = O(n) 0->1->2 … target Space: O(n)
            cur_level = queue.popleft() #[3]
            next_level = []
            for word in cur_level:
                for j in range(n):
                    if j == target and graph[word][j]:
                        return hop + 2
                    if graph[word][j]:
                        graph[word][j] = 0
                        graph[j][word] = 0
                        next_level.append(j)
            if next_level:
                queue.append(next_level)
            hop += 1
        return 0