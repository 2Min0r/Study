# [digit_reverse.py]
# 자연수 뒤집어 배열로 만들기

# first
def solution1(n):
    answer = [int(i) for i in str(n)]
    return answer[::-1]