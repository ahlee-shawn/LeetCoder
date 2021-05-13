class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m*n-1
        while start <= end:
            if matrix[(start-1) // n][(start-1) % n] == target or matrix[(end-1) // n][(end-1) % n] == target:
                return True
            mid = start + ((end - start) // 2)
            if matrix[(mid-1) // n][(mid-1) % n] > target:
                end = mid - 1
            elif matrix[(mid-1) // n][(mid-1) % n] < target:
                start = mid + 1
            else:
                return True
        return False