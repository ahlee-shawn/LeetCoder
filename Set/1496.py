class Solution:
    def isPathCrossing(self, path: str) -> bool:
        table = set()
        x = y = 0
        table.add((x, y))
        for i in range(len(path)):
            if path[i] == 'N':
                y += 1
            elif path[i] == 'S':
                y -= 1
            elif path[i] == 'E':
                x += 1
            elif path[i] == 'W':
                x -= 1
            if (x, y) not in table:
                table.add((x, y))
            else:
                return True
        return False