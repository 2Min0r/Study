# [targetnumber.py]
# 타겟넘버

from itertools import combinations

def solution(numbers, target):
    answer = 0
    for i in range(0, len(numbers)-1):
        for j in list(combinations(numbers, i)):
            if sum(j) == (sum(numbers)-target)//2:
                answer +=1
    return answer