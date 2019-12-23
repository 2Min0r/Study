# coding: utf-8
import time
import random

def max_profit_slow(prices):
    n = len(prices)
    max_porofit = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > max_porofit:
                max_porofit = profit
    return max_porofit

def max_profit_fast(prices):
    n = len(prices)
    min_prices = prices[0]
    max_profit = 0
    
    for i in range(0 , n):
        if min_prices > prices[i]:
            min_prices = prices[i]
        profit = prices[i] - min_prices
        if max_profit < profit:
            max_profit = profit
    return max_profit

def test(n):
    a = []
    for i in range(0, n):
        a.append(random.randint(5000, 20000))
    
    # max_profit_slow Algorithm test
    start = time.time()
    mps = max_profit_slow(a)
    end = time.time()
    time_slow = end - start

    # max_profit_fast Algorithm test
    start = time.time()
    mpf = max_profit_fast(a)
    end = time.time()
    time_fast = end - start

    # result
    print(n, mps, mpf)
    m = 0
    if time_fast > 0:
        m = time_slow / time_fast
    print("%d %.5f %.5f %.2f" % (n, time_slow, time_fast, m))

test(100)
test(10000)
test(100000)