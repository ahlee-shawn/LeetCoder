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

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        while num != 0:
            if num >= 1000:
                ans += 'M'
                num -= 1000
            elif num >= 900:
                ans += 'CM'
                num -= 900
            elif num >= 500:
                ans += 'D'
                num -= 500
            elif num >= 400:
                ans += 'CD'
                num -= 400
            elif num >= 100:
                ans += 'C'
                num -= 100
            elif num >= 90:
                ans += 'XC'
                num -= 90
            elif num >= 50:
                ans += 'L'
                num -= 50
            elif num >= 40:
                ans += 'XL'
                num -= 40
            elif num >= 10:
                ans += 'X'
                num -= 10
            elif num >= 9:
                ans += 'IX'
                num -= 9
            elif num >= 5:
                ans += 'V'
                num -= 5
            elif num >= 4:
                ans += 'IV'
                num -= 4
            else:
                ans += 'I'
                num -= 1
        return ans