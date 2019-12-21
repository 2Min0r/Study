# coding: utf-8

# O(n^2)
def my_bubble_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        for j in range (i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    return a

# O(n^2)
def bubble_sort(a):
    n = len(a)
    while True:
        changed = False
        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True
        if changed == False:
            return

d1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
my_bubble_sort(d1)
print("d1", d1)

d2 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
bubble_sort(d2)
print("d2", d2)