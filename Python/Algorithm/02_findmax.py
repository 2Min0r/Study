# coding: utf-8

# O(n) : 비교 횟수가 n -1 이므로
def find_max(a):
    n = len(a)
    max = a[0]
    for i in range(1, n):
        if max < a[i]:
            max = a[i]
    return max

# O(n) : 비교 횟수가 n - 1이므로
def find_max_index(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[max_idx] < a[i]:
            max_idx = i
    return max_idx

a = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(a))
print(find_max_index(a))