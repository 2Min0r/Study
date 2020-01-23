# [adder.py]
# 두 정수 사이의 합

# First code
def solution1(a, b):
    if a <= b:
        answer = sum(list(range(a, b+1)))
    else:
        answer = sum(list(range(b, a+1)))
    return answer

# Improved code
def solution2(a, b):
    answer = sum(list(range(min(a,b), max(a,b)+1)))
    return answer