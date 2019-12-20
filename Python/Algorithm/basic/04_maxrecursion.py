# coding: utf-8

# O(n) ??
def max_recursion(a, n):
    if n == 1:
        return a[0]
    max = max_recursion(a, n - 1)

    if max > a [n - 1]:
        return max
    else:
        return a[n - 1]


v = [17, 92, 18, 33, 58, 7, 33, 42]

print(max_recursion(v, len(v)))