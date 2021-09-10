class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for i in range(n - 1):
            p = q = 0
            length = len(ans)
            temp = ""
            while p < length:
                q = p + 1
                while q < length and ans[p] == ans[q]:
                    q += 1
                temp += (str(q - p) + ans[p])
                p = q
            ans = temp
        return ans