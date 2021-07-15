class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        c = 0
        ans = ""
        offset = ord('0')
        if len(num1) < len(num2):
            a, b = num2, num1
        else:
            a, b = num1, num2
        for i in range(1, len(b)+1):
            temp = (ord(a[-i]) - offset) + (ord(b[-i]) - offset) + c
            if temp > 9:
                c = 1
                temp -= 10
            else:
                c = 0
            ans = chr(temp + offset) + ans
        for i in range(len(b)+1, len(a)+1):
            temp = (ord(a[-i]) - offset) + c
            if temp > 9:
                c = 1
                temp -= 10
            else:
                c = 0
            ans = chr(temp + offset) + ans
        if c:
            ans = "1" + ans
        return ans