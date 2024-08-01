from typing import List
import heapq
def getNumberOfBacklogOrders(orders: List[List[int]]) -> int:
    MOD = 10**9 + 7

    buy_heap = []  # max-heap (invert prices to use with heapq)
    sell_heap = []  # min-heap

    for price, amount, orderType in orders:
        if orderType == 0:  # Buy order
            while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                sell_price, sell_amount = heapq.heappop(sell_heap)
                if sell_amount > amount:
                    heapq.heappush(sell_heap, (sell_price, sell_amount - amount))
                    amount = 0
                else:
                    amount -= sell_amount
            if amount > 0:
                heapq.heappush(buy_heap, (-price, amount))
        else:  # Sell order
            while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                buy_price, buy_amount = heapq.heappop(buy_heap)
                if buy_amount > amount:
                    heapq.heappush(buy_heap, (buy_price, buy_amount - amount))
                    amount = 0
                else:
                    amount -= buy_amount
            if amount > 0:
                heapq.heappush(sell_heap, (price, amount))

    total_orders = 0
    for _, amount in buy_heap:
        total_orders = (total_orders + amount) % MOD
    for _, amount in sell_heap:
        total_orders = (total_orders + amount) % MOD

    return total_orders


getNumberOfBacklogOrders([[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]])
