class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            if rowIndex == 0:
                return [1]
            if rowIndex == 1:
                return [1, 1]
        ans = [1,2,1]
        for i in range(2, rowIndex):
            for j in range(len(ans)-1):
                ans[j] += ans[j+1]
            ans[-1] = 1
            ans.insert(0,1)
        return ans