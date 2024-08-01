from typing import List

def maxProfit(prices: List[int]) -> int:
    i=0
    profit = 0
    if len(prices) > 1:
        while i <= len(prices):
            if prices[i] < prices[i + 1]:
                profit = profit + prices[i + 1] - prices[i]
            i += 1
            if i == len(prices)-1:
                break
            
    return profit

p = maxProfit([7, 1, 5, 3, 6, 4])

print(p) # Output: 5
        