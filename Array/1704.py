class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 0
        s = s.lower()
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        for i in range(int(len(s)/2)):
            if s[i] in vowel_list:
                vowels += 1
        for i in range(int(len(s)/2), len(s)):
            if s[i] in vowel_list:
                vowels -= 1
        if vowels:
            return False
        return True