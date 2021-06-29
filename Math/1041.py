class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        face = 0
        for i in range(len(instructions)):
            if instructions[i] == "L":
                face += 3
                face %= 4
            elif instructions[i] == "R":
                face += 1
                face %= 4
            elif instructions[i] == "G":
                if face == 0:
                    y += 1
                elif face == 1:
                    x += 1
                elif face == 2:
                    y -= 1
                elif face == 3:
                    x -= 1
        if (x == 0 and y == 0) or face != 0:
            return True
        return False