# coding: utf-8

# O(n^2)
def paring(a):
    n = len(a)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            print(a[i], "-",  a[j])

name = ["Tom", "Jerry", "Mike"]
paring(name)

print()

name2 = ["Tom", "Jerry", "Mike", "John"]
paring(name2)