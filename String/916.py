class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ans = []
        b_table = dict()
        for b in B:
            for char in b:
                if char not in b_table or b_table[char] < b.count(char):
                    b_table[char] = b.count(char)
        
        for a in A:
            b_char_all_in_a = True
            for b in b_table:
                if a.count(b) < b_table[b]:
                    b_char_all_in_a = False
                    break
            if b_char_all_in_a:
                ans.append(a)
        
        return ans