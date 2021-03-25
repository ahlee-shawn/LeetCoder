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