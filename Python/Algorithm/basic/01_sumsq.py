# coding: utf-8

# O(1) : 계산횟수가 6이므로
def sum_sq(n):
    return n* (n + 1) * (2 * n + 1) // 6

print(sum_sq(10))