class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        
        def dfs(S, current_string, index, ans):
            if index == len(S):
                ans.append(current_string)
                return ans
            if S[index].isdigit():
                ans = dfs(S, current_string+S[index], index+1, ans)
            else:
                ans = dfs(S, current_string+S[index].lower(), index+1, ans)
                ans = dfs(S, current_string+S[index].capitalize(), index+1, ans)
            return ans
        
        return dfs(S, "", 0, ans)