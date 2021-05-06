class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = dict()
        ans = []
        index = 0
        for string in strs:
            charCount = [0 for _ in range(26)]
            for char in string:
                charCount[ord(char)-ord('a')] += 1
            key = tuple(charCount)
            if key not in table:
                table[key] = index
                ans.append([string])
                index += 1
            else:
                ans[table[key]].append(string)
        return ans