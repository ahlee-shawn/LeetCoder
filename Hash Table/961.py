class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        encountered_numbers = {}
        for i in A:
            if i in encountered_numbers:
                return i
            else:
                encountered_numbers[i] = 1