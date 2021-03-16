class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        table = dict()
        table['a'] = 0
        table['b'] = 0
        table['l'] = 0
        table['n'] = 0
        table['o'] = 0
        
        for i in range(len(text)):
            if text[i] in table:
                table[text[i]] += 1
        
        a = table['a']
        b = table['b']
        l = int(table['l'] / 2)
        n = table['n']
        o = int(table['o'] / 2)
        
        return min(a, b, l, n, o)