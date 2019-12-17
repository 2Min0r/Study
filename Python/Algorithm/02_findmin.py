# coding: utf-8

# O(n): 비교 횟수가 n -1 이므로
def find_min(a):
    n = len(a)
    min_v = a[0]

    for i in range(1, n):
        if min_v > a[i]:
            min_v = a[i]
    return min_v

a = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(a))