# coding: utf-8

# O(n)
def sum_recursion(n):
    if n <= 1:
        return 1
    else:
        return n + sum_recursion(n - 1)

print(sum_recursion(10))