# coding: utf-8

# O(min(a,b))
def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        else:
            i = i -1

# 유클리드 알고리즘 이용하기 O(n^2)
def r_gcd(a, b):
    if b == 0:
        return a
    return r_gcd(b, a % b)



print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))

print()

print(r_gcd(1, 5))
print(r_gcd(3, 6))
print(r_gcd(60, 24))
print(r_gcd(81, 27))