import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        r = sqrt(random.uniform(0, 1))*self.r
        degree = random.uniform(0, 2)
        x = self.x + r*math.cos(math.pi*degree)
        y = self.y + r*math.sin(math.pi*degree)
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()