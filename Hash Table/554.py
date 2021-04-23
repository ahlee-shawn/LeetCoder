class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        table = dict()
        for i in range(len(wall)):
            prev_length = 0
            for j in range(len(wall[i]) - 1):
                prev_length += wall[i][j]
                if prev_length not in table:
                    table[prev_length] = 1
                else:
                    table[prev_length] += 1
        max_num = 0
        for key in table:
            max_num = max(max_num, table[key])
        return len(wall) - max_num