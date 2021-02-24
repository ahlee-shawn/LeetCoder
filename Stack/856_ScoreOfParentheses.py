class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        score = 0
        stack = []
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2*score, 1)
        return score