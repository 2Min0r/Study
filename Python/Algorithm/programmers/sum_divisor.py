# [sum_divisor.py]
# 약수의 합

# first
def solution1(n):
    arr = []

    for i in range(1, n+1) :
        if n % i == 0 :
            arr.append(i)


    return sum(arr)