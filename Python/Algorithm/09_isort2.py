# coding: utf-8

# O(n^2)
def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >=0 and a[j] > key:                 # 내림차순 정렬로 바꾸려면 부호 변경
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key

    return a


d = [2, 4, 5, 1, 3]

print(ins_sort(d))