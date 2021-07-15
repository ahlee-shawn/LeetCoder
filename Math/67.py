class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        ans = ""
        offset = ord('0')
        if len(a) < len(b):
            a, b = b, a
        for i in range(1, len(b)+1):
            temp = (ord(a[-i]) - offset) + (ord(b[-i]) - offset) + c
            if temp > 1:
                c = 1
                temp -= 2
            else:
                c = 0
            ans = chr(temp + offset) + ans
        for i in range(len(b)+1, len(a)+1):
            temp = (ord(a[-i]) - offset) + c
            if temp > 1:
                c = 1
                temp -= 2
            else:
                c = 0
            ans = chr(temp + offset) + ans
        if c:
            ans = "1" + ans
        return ans