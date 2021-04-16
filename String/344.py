class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        high, low = len(s)-1, 0
        while high > low:
            s[high], s[low] = s[low], s[high]
            high -= 1
            low += 1