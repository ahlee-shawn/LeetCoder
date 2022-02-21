class Solution:
    def bfs(self, matrix, queue, table):
        m = len(matrix)
        n = len(matrix[0])
        while queue:
            current_index = queue.pop(0)
            current_x = current_index[0]
            current_y = current_index[1]
            current_value = matrix[current_x][current_y]
            # up
            if current_x > 0:
                if current_value <= matrix[current_x-1][current_y] and table[current_x-1][current_y] == 0:
                    queue.append([current_x-1,current_y])
                    table[current_x-1][current_y] = 1
            # down
            if current_x < m-1:
                if current_value <= matrix[current_x+1][current_y] and table[current_x+1][current_y] == 0:
                    queue.append([current_x+1,current_y])
                    table[current_x+1][current_y] = 1
            # left
            if current_y > 0:
                if current_value <= matrix[current_x][current_y-1] and table[current_x][current_y-1] == 0:
                    queue.append([current_x,current_y-1])
                    table[current_x][current_y-1] = 1
            # right
            if current_y < n-1:
                if current_value <= matrix[current_x][current_y+1] and table[current_x][current_y+1] == 0:
                    queue.append([current_x,current_y+1])
                    table[current_x][current_y+1] = 1
        return table

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix == []:
            return []
        m = len(matrix)
        n = len(matrix[0])
        print(m, n)
        # 1: able 0: unknown/unable
        # initialize pacific table
        queue = []
        pacific_table = [ [0]*n for i in range(m)]
        for i in range(n):
            queue.append([0,i])
            pacific_table[0][i] = 1
        for i in range(1,m):
            queue.append([i,0])
            pacific_table[i][0] = 1
        pacific_table = self.bfs(matrix, queue, pacific_table)
        
        queue = []
        atlantic_table = [ [0]*n for i in range(m)]
        for i in range(n-1):
            queue.append([m-1,i])
            atlantic_table[m-1][i] = 1
        for i in range(m):
            queue.append([i,n-1])
            atlantic_table[i][n-1] = 1
        atlantic_table = self.bfs(matrix, queue, atlantic_table)
        
        ans = []
        for i in range(m):
            for j in range(n):
                if pacific_table[i][j] and atlantic_table[i][j]:
                    ans.append([i,j])
        return ans

class Solution:
    def initialize(self, isPacific, m, n):
        queue = deque()
        table = set()
        rowIndex = 0 if isPacific else m-1
        colIndex = 0 if isPacific else n-1
        nextLevel = []
        for i in range(n):
            nextLevel.append([rowIndex, i])
            table.add((rowIndex, i))
        for i in range(0+isPacific, m-1+isPacific):
            nextLevel.append([i, colIndex])
            table.add((i, colIndex))
        queue.append(nextLevel)
        return queue, table
    
    def bfs(self, heights, isPacific):
        m, n = len(heights), len(heights[0])
        queue, table = self.initialize(isPacific, m, n)
        while queue:
            currentLevel = queue.popleft()
            nextLevel = []
            for (i, j) in currentLevel:
                currentHeight = heights[i][j]
                # Up
                if i > 0 and heights[i-1][j] >= currentHeight and (i-1, j) not in table:
                    nextLevel.append([i-1, j])
                    table.add((i-1, j))
                # Down
                if i < m-1 and heights[i+1][j] >= currentHeight and (i+1, j) not in table:
                    nextLevel.append([i+1, j])
                    table.add((i+1, j))
                # Left
                if j > 0 and heights[i][j-1] >= currentHeight and (i, j-1) not in table:
                    nextLevel.append([i, j-1])
                    table.add((i, j-1))
                # Right
                if j < n-1 and heights[i][j+1] >= currentHeight and (i, j+1) not in table:
                    nextLevel.append([i, j+1])
                    table.add((i, j+1))
            if nextLevel:
                queue.append(nextLevel)
        return table
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        pacific = self.bfs(heights, True)
        atlantic = self.bfs(heights, False)
        for element in atlantic.intersection(pacific):
            ans.append([element[0], element[1]])
        return ans