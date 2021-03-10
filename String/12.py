class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        index = 0
        while True:
            if num >= num_list[index]:
                num -= num_list[index]
                ans += roman_list[index]
            else:
                index += 1
            if num == 0:
                return ans