# [sum_digit.py]
# 자릿수 더하기

# first
def solution1(n):
    answer = 0
    for i in str(n):
        answer += ord(i)-48
    return answer

# second
def solution2(n):
    if n < 10:
        return n % 10
    return n % 10 + solution(n//10)