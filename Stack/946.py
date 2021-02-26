class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while True:
            move = 0
            if (not pushed) and (not popped) and (not stack):
                return True
            
            if not stack:
                move = 1
                stack.append(pushed.pop(0))
            
            if popped[0] == stack[-1]:
                move = 1
                popped.pop(0)
                stack.pop(-1)
            elif pushed:
                move = 1
                stack.append(pushed.pop(0))
            
            if move == 0:
                return False