class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        duplicate = 1
        for char in s:
            if not stack or stack[-1][0] != char:
                duplicate = 1
                stack.append([char, duplicate])
            else:
                if stack[-1][1] != k-1:
                    duplicate += 1
                    stack.append([char, duplicate])
                else:
                    for i in range(k-1):
                        stack.pop(-1)
                    if stack:
                        duplicate = stack[-1][1]
                    else:
                        duplicate = 1
        ans = ""
        for i in range(len(stack)):
            ans += stack[i][0]
        return ans