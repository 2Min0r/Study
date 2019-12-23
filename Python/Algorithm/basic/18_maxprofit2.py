# coding: utf-8

# O(n)
def max_profit(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]
    for i in range(0, n):
        if min_price > prices[i]:
            min_price = prices[i]
        profit = prices[i] - min_price
        if max_profit < profit:
            max_profit = profit
    return max_profit





stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))        #2400