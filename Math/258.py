class Solution:
    def recursion(self, num):
        if num < 10:
            return num
        digit_sum = 0
        while True:
            digit_sum += (num % 10)
            num = num // 10
            if num == 0:
                break
        return self.recursion(digit_sum)
    def addDigits(self, num: int) -> int:
        return self.recursion(num)