# [number_generator.py]
# x만큼 간격이 있는 n개의 숫자

# first
def solution1(x, n):
    if x == 0:
        return [0] * n
    return [i for i in range(x, x * (n + 1), x)]

# second
def solution2(x, n):
    return [i * x + n for i in range(n)]