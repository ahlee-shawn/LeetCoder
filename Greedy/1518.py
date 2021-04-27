class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        ans = 0
        while True:
            if full:
                ans += full
                empty += full
                full = 0
            elif empty >= numExchange:
                full += (empty // numExchange)
                empty %= numExchange
            else:
                break
        return ans