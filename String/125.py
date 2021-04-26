class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        alphanumeric = []
        for i in range(48, 58):
            alphanumeric.append(i)
        for i in range(65, 91):
            alphanumeric.append(i)
        for i in range(97, 123):
            alphanumeric.append(i)
        while left < right:
            if ord(s[left]) not in alphanumeric:
                left += 1
            elif ord(s[right]) not in alphanumeric:
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True