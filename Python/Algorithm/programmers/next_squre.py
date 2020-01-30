# [next_squre.py]
# 정수 제곱근 판별

# first
from math import sqrt
def solution1(n):
    if int(sqrt(n))**2 == n:
        return (int(sqrt(n))+1)**2
    else:
        return -1

# second
def solution2(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return (sqrt+1)**2
    else:
        return -1