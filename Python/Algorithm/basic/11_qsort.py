# coding: utf-8
# O(n * log n)
def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    
    pivot = a[-1]                   # 리스트의 마지막 값
    g1 = []
    g2 = []
    for i in range(0, n - 1):       # 마지막은 pivot값
        if a[i] < pivot:            # 내림차순 정렬은 부호 변경
            g1.append(a[i])
        else:
            g2.append(a[i])

    return quick_sort(g1) + [pivot] + quick_sort(g2)

a = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(a))