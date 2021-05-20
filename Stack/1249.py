class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop(-1)
                else:
                    s[i] = ''
        if stack:
            for index in stack:
                s[index] = ''
        return ''.join(s)