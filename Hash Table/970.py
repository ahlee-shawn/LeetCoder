class Solution:
    def powers_of_num(self, num, bound):
        ans = [1]
        while True and num != 1:
            temp = ans[-1]*num
            if temp < bound:
                ans.append(temp)
            else:
                break
        return ans
    
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        x_list = self.powers_of_num(x, bound)
        y_list = self.powers_of_num(y, bound)
        table = set()
        for i in range(len(x_list)):
            for j in range(len(y_list)):
                temp = x_list[i] + y_list[j]
                if temp <= bound and temp not in table:
                    table.add(temp)
        return list(table)