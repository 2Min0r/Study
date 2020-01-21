# [cleardivison.py]
# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    answer.sort()
    if answer == []:
        answer=[-1]
    return answer