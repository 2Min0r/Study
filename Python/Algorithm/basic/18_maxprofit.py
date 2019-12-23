# coding: utf-8

# 주식 한 주를 한 번 사고 팔아 얻을 수 있는 최대 이익
# O(n^2)

def max_profit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if max_profit < profit:
                max_profit = profit
    return max_profit


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))        #2400