from typing import List
def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        buying_price = prices[0]
        for price in prices[1:]:
            if price > buying_price:
                max_profit = max(max_profit, price- buying_price)
            else:
                buying_price = price
        return max_profit
