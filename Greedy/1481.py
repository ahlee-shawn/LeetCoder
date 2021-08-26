class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        table = dict()
        for num in arr:
            if num not in table:
                table[num] = 1
            else:
                table[num] += 1
        for key in sorted(table, key=table.get):
            if table[key] <= k:
                k -= table[key]
                del table[key]
            else:
                break
        return len(table)