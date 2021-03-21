class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == 'c':
                if len(stack) < 2:
                    return False
                stack_top = stack.pop(-1)
                if stack_top != 'b':
                    return False
                stack_top = stack.pop(-1)
                if stack_top != 'a':
                    return False
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        else:
            return False