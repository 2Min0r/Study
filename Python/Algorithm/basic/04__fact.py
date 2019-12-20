# coding: utf-8

# O(n)
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

# O(n)
def fact_recursion(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recursion(n - 1)

print(fact(1))
print(fact(5))
print(fact(10))

print(fact_recursion(1))
print(fact_recursion(5))
print(fact_recursion(10))