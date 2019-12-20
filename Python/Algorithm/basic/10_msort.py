# coding: utf-8

# O(n * log n)
def merge_sort(a):
    n = len(a)
    
    if n <= 1:
        return a

    mid = n // 2
    g1 = merge_sort(a[:mid])            # :mid 를 통해 mid 직전까지의 자료를 복사해서 새 리스트를 만듦
    g2 = merge_sort(a[mid:])            # mid: 를 통해 mid부터 끝까지의 자료를 복사해서 새 리스트를 만듦

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    
    # 남아있는 자료 추가
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))

    return result


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(merge_sort(d))