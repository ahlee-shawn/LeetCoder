# Set
class Solution:
    def calculate_sum_of_the_squares_of_digits(self, n):
        return_sum = 0
        while n > 0:
            digit = n % 10
            return_sum += ((digit)**2)
            n = n // 10
        return return_sum
    def isHappy(self, n: int) -> bool:
        table = set()
        while True:
            n = self.calculate_sum_of_the_squares_of_digits(n)
            if n == 1:
                return True
            if n not in table:
                table.add(n)
            else:
                return False

# Faster
class Solution:
    def calculate_sum_of_the_squares_of_digits(self, n):
        return_sum = 0
        while n > 0:
            digit = n % 10
            return_sum += ((digit)**2)
            n = n // 10
        return return_sum
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self.calculate_sum_of_the_squares_of_digits(slow)
            fast = self.calculate_sum_of_the_squares_of_digits(fast)
            fast = self.calculate_sum_of_the_squares_of_digits(fast)
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False