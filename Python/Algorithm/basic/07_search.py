# coding: utf-8

# O(n)
def search_list(a, x):
    n = len(a)
    result = []
    for i in range(0, n):
        if a[i] == x:
            result.append(i)
    return result

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))
