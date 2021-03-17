class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = prices[-1]
        profit = 0
        for price in prices[::-1]:
            if max_price - price > profit:
                profit = max_price - price
            if price > max_price:
                max_price = price
        return profit