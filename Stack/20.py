class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {'(': ')', '[': ']', '{': '}'}
        left_set = set(['(', '[', '{'])
        for char in s:
            if char in left_set:
                stack.append(char)
            elif stack and char == table[stack[-1]]:
                stack.pop(-1)
            else:
                return False
        return stack == []