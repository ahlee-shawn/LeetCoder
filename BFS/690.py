"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        table = dict() # id -> index
        for i in range(len(employees)):
            table[employees[i].id] = i
        ans = 0
        queue = deque()
        queue.append(id)
        while queue:
            current_id = queue.popleft()
            index = table[current_id]
            ans += employees[index].importance
            queue.extend(employees[index].subordinates)
        return ans