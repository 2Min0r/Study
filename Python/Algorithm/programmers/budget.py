# [budget.py]
# 예산

def solution(d, budget):
    d.sort()
    for count, money in enumerate(d):
        budget -= money
        if budget < 0:
            return count
    return len(d)