class Solution:
    def removeOneDigit(self, num):
        for i in range(1, len(num)): # O(n), n = len(input num)
            if num[i] < num[i-1]:
                # [0 : i-1: ]
                # remove the (i-1)th digit
                return num[: i-1] + num[i:]
        # 12345
        # remove the last digit
        return num[:-1]

    # num = "000"
    # count = 3
    def removeLeadingZeros(self, num):
        count = 0
        for i in range(len(num)):
            if num[i] == "0":
                count += 1
            else:
                break
        if count == len(num):
            return "0"
        else:
            return num[count:]

    def removeKdigits(self, num: str, k: int) -> str:
        # input num length = n
        for i in range(k): # O(k)
            num = self.removeOneDigit(num)
        num = self.removeLeadingZeros(num)
        return num
# Time: O(nk - k^2)
# Space: O(n)
