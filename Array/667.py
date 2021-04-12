class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = []
        start = 1
        end = n
        for i in range(k - 1):
            if i % 2:
                ans.append(end)
                end -= 1
            else:
                ans.append(start)
                start += 1
        if k % 2:
            for i in range(start, end+1):
                ans.append(i)
        else:
            for i in range(end, start-1, -1):
                ans.append(i)
        return ans