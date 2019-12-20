# coding: utf-8

# O(n^2)
def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)                               # r은 v가 들어가지 않은 상태, 마지막 자리에 새로 값을 넣으므로 len(r)의 idx

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return result


d = [2, 4, 5, 1, 3]

print(ins_sort(d))