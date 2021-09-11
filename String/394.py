class Solution:
    def isDigit(self, c): 
        return 0 <= ord(c) - ord('0') <= 9

    def decodeString(self, s: str) -> str:
        i = 0
        n = len(s)
        stack = []
        while i < n: #O(n)
            if self.isDigit(s[i]):
                #Digit
                j = i + 1
                while j < n and self.isDigit(s[j]):
                    j += 1
                stack.append(s[i:j])
                i = j
            elif s[i] == '[':
                stack.append('[')
                i += 1
            elif s[i] == ']':
                string_btwn_brackets = ""
                while True: #O(n)
                    popped_value = stack.pop()
                    if popped_value == '[':
                        break
                    string_btwn_brackets = popped_value + string_btwn_brackets
                number = int(stack.pop())
                temp = ""
                for j in range(number): #O(10 ^ (n-3)), (maxK ^ countK *n)
                    temp += string_btwn_brackets
                stack.append(temp)
                i += 1
            else:
                #char
                stack.append(s[i])
                i += 1
        return "".join(stack)