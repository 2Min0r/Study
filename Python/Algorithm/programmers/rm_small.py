# [rm_small.py]
# 제일 작은 수 제거하기

# first
def solution1(arr):
    if len(arr) >1:
        arr.remove(min(arr))
    else:
        return [-1]
    return arr