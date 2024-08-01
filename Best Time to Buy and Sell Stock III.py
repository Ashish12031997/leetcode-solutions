
from typing import List
def maxProfit(prices: List[int]) -> int:
    buy = prices[0]
    max_profit = []
    for sell in prices[1:]:
        if sell > buy:
            max_profit.append(sell-buy)
        buy = sell
    print(max_profit)
    return sum(sorted(max_profit, reverse=True)[0:2])


a = maxProfit([3,3,5,0,0,3,1,4])

print(a)
