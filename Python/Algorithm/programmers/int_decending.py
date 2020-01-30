# [int_decending.py]
# 정수 내림차순으로 배치하기

# first
def solution1(n):
    ans = [int(c) for c in str(n)]
    ans.sort(reverse=True)
    return int(''.join(map(str,ans)))

# second
def solution2(n):
    ans = list(str(n))
    ans.sort(reverse=True)
    return int(''.join(map(str,ans)))