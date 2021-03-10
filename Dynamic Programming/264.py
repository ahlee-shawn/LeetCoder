class Solution:
    def nthUglyNumber(self, n: int) -> int:
        counter, p2, p3, p5 = 0, 0, 0, 0
        ans = [1]
        while counter < n:
            ans.append(min(ans[p2]*2, ans[p3]*3, ans[p5]*5))
            if ans[-1] == ans[p2]*2:
                p2 += 1
            if ans[-1] == ans[p3]*3:
                p3 += 1
            if ans[-1] == ans[p5]*5:
                p5 += 1
            counter += 1
        
        return ans[n-1]