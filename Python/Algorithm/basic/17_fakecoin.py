# coding: utf-8

# weigh에서 하는 일을 find_fakecoin이 모른다면,
# a == fake or b == fake 일때 -1을 주고 c == fake or d == fake 일때 1을 주는 것과 똑같은데 왜 저렇게 쓰는걸까?

# O(n)

def weigh(a, b, c, d):
    fake = 29
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1

    return 0

def find_fakecoin(left, right):
    for i in range(left + 1, right + 1):
        result = weigh(left, left, i, i)
        if result == -1:
            return left
        elif result == 1:
            return i

    return -1

n = 100
print(find_fakecoin(0, n - 1))