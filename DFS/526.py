class Solution:
    def dfs(self, i, avail_num):
        if i == 1:
            return 1
        cur_prem = 0
        for num in avail_num:
            if num % i == 0 or i % num == 0:
                new_avail_num = avail_num.copy()
                new_avail_num.remove(num)
                cur_prem += self.dfs(i-1, new_avail_num)
        return cur_prem
        
    def countArrangement(self, n: int) -> int:
        return self.dfs(n, set(range(1, n+1)))