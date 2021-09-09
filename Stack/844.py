class Solution:
    def simulate(self, a):
        stack = []
        for i in range(len(a)):
            if a[i] == '#':
                if len(stack):
                    stack.pop()
            else:
                stack.append(a[i])
        return stack
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = self.simulate(s)
        stack_t = self.simulate(t)
        return stack_s == stack_t
        