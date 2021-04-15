class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] == 10:
            i = -1
            while True:
                try:
                    digits[i] -= 10
                    digits[i-1] += 1
                    if digits[i-1] < 10:
                        break
                    i -= 1
                except:
                    digits.insert(0, 1)
                    break
        return digits