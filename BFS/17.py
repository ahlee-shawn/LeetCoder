class Solution:
    def bfs(self, index, digits, ans):
        if index == len(digits):
            return ans
        
        while True:
            sub_string = ans.pop(0)
            if len(sub_string) > index:
                ans.append(sub_string)
                break
            if digits[index] == '2':
                ans.append(sub_string+'a')
                ans.append(sub_string+'b')
                ans.append(sub_string+'c')
            if digits[index] == '3':
                ans.append(sub_string+'d')
                ans.append(sub_string+'e')
                ans.append(sub_string+'f')
            if digits[index] == '4':
                ans.append(sub_string+'g')
                ans.append(sub_string+'h')
                ans.append(sub_string+'i')
            if digits[index] == '5':
                ans.append(sub_string+'j')
                ans.append(sub_string+'k')
                ans.append(sub_string+'l')
            if digits[index] == '6':
                ans.append(sub_string+'m')
                ans.append(sub_string+'n')
                ans.append(sub_string+'o')
            if digits[index] == '7':
                ans.append(sub_string+'p')
                ans.append(sub_string+'q')
                ans.append(sub_string+'r')
                ans.append(sub_string+'s')
            if digits[index] == '8':
                ans.append(sub_string+'t')
                ans.append(sub_string+'u')
                ans.append(sub_string+'v')
            if digits[index] == '9':
                ans.append(sub_string+'w')
                ans.append(sub_string+'x')
                ans.append(sub_string+'y')
                ans.append(sub_string+'z')
        
        return self.bfs(index+1, digits, ans)
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        ans = [""]
        return self.bfs(0, digits, ans)