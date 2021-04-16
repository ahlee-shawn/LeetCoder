class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in range(0, len(S)):
            if len(stack) == 0 or S[i] != stack[-1]:
                stack.append(S[i])
            else:
                stack.pop(-1)
        ans = ""
        for i in stack:
            ans += i
        return ans