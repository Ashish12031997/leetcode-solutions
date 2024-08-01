def stockmax(prices):
    max_profit = 0
    max_future_price = 0
    
    for price in reversed(prices):
        if price > max_future_price:
            max_future_price = price
        max_profit += max_future_price - price
    
    return max_profit


a = stockmax([1, 2, 100])
print(a)
