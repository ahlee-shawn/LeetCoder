class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_splitted = path.split('/')
        for i in range(len(path_splitted)):
            # /home//user
            # ['', 'home', '']
            if len(path_splitted[i]) > 0: # not //
                if path_splitted[i] == '.':
                    continue
                elif path_splitted[i] == '..':
                    if stack:
                        stack.pop(-1)
                else:
                    stack.append(path_splitted[i])
        ans = "/"
        if stack:
            for i in range(len(stack)):
                ans += (stack[i] + '/')
            return ans[:-1]
        return ans