# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n) == 0:
            return n
        high, low = n, 1
        guess_number = n // 2
        while True:
            result = guess(guess_number)
            if result == 0:
                return guess_number
            elif result == 1:
                low = guess_number
                guess_number = (guess_number + high) // 2
            else:
                high = guess_number
                guess_number = (guess_number + low) // 2