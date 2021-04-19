class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1], [1,1]]
        for i in range(numRows - 2):
            prev = ans[-1]
            temp = [1]
            for j in range(len(prev)-1):
                temp.append(prev[j]+prev[j+1])
            temp.append(1)
            ans.append(temp)
        return ans