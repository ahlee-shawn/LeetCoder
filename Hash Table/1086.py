class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        table = dict()
        for item in items:
            student, score = item[0], item[1]
            if student not in table:
                table[student] = [score]
            else:
                heapq.heappush(table[student], score)
                if len(table[student]) > 5:
                    heapq.heappop(table[student])
        ans = []
        for record in sorted(table.items()):
            average = sum(record[1]) // 5
            ans.append([record[0], average])
        return ans