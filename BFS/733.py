class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]
        queue = deque()
        queue.append([sr, sc])
        while queue:
            node = queue.popleft()
            i, j = node[0], node[1]
            image[i][j] = newColor
            # left:
            if j != 0 and image[i][j - 1] == original_color and image[i][j - 1] != newColor:
                queue.append([i, j - 1])
            # right:
            if j != n - 1 and image[i][j + 1] == original_color and image[i][j + 1] != newColor:
                queue.append([i, j + 1])
            # up:
            if i != 0 and image[i - 1][j] == original_color and image[i - 1][j] != newColor:
                queue.append([i - 1, j])
            # down:
            if i != m - 1 and image[i + 1][j] == original_color and image[i + 1][j] != newColor:
                queue.append([i + 1, j])
        return image