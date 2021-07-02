class Solution:
    def __init__(self):
        self.ans = []
        
    def valid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                if len(stack) and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False
        return True
        
    def dfs(self, s, left, right, start):
        if left < 0 or right < 0:
            return
        if left == right == 0 and self.valid(s):
            self.ans.append(s)
        else:
            for i in range(start, len(s)):
                if right and s[i] == ')':
                    if i == 0 or s[i-1] != ')':
                        self.dfs(s[:i]+s[i+1:], left, right-1, i)
            for i in range(start, len(s)):
                if left and s[i] == '(':
                    if i == 0 or s[i-1] != '(':
                        self.dfs(s[:i]+s[i+1:], left-1, right, i)
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                if left:
                    left -= 1
                else:
                    right += 1
        self.dfs(s, left, right, 0)
        if not self.ans:
            self.ans = [""]
        return self.ans