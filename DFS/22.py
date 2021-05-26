class Solution:
    
    def __init__(self):
        self.ans = []
    
    def helper(self, n, state, left, right):
        if len(state) == 2*n:
            self.ans.append(''.join(state))
            return
        if left < n:
            state.append('(')
            self.helper(n, state, left+1, right)
            state.pop(-1)
        if right < left:
            state.append(')')
            self.helper(n, state, left, right+1)
            state.pop(-1)
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.helper(n, [], 0, 0)
        return self.ans