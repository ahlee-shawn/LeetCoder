import numpy as np

class Solution:
    
    def count_number_occurrence(self, char_count, number_count, distinguish_term, number, english):
        occurrence = char_count[ord(distinguish_term)-ord('a')]
        number_count[number] += occurrence
        for i in range(len(str(english))):
            char_count[ord(english[i])-ord('a')] -= occurrence
        return char_count, number_count
    
    def originalDigits(self, s: str) -> str:
        number_count = np.zeros(10, dtype=int)
        char_count = np.zeros(26, dtype=int)
        for i in range(len(s)):
            char_count[ord(s[i])-ord('a')] += 1
        char_count, number_count = self.count_number_occurrence(char_count, number_count, 'z', 0, 'zero')
        char_count, number_count = self.count_number_occurrence(char_count, number_count, 'g', 8, 'eight')
        char_count, number_count = self.count_number_occurrence(char_count, number_count, 'x', 6, 'six')
        char_count, number_count = self.count_number_occurrence(char_count, number_count, 's', 7, 'seven')
        char_count, number_count = self.count_number_occurrence(char_count, number_count, 'v', 5, 'five')
        char_count, number_count = self.count_number_occurrence(char_count, number_count, 'f', 4, 'four')
        char_count, number_count = self.count_number_occurrence(char_count, number_count, 'i', 9, 'nine')
        char_count, number_count = self.count_number_occurrence(char_count, number_count, 'r', 3, 'three')
        char_count, number_count = self.count_number_occurrence(char_count, number_count, 'w', 2, 'two')
        char_count, number_count = self.count_number_occurrence(char_count, number_count, 'e', 1, 'one')
        
        ans = ''
        for i in range(10):
            for j in range(number_count[i]):
                ans += str(i)
        return ans