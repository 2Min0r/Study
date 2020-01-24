# [decending.py]
# 문자열 내림차순으로 배치하기

# First
def solution1(s):
    s = sorted(s)
    answer = ""
    for i in range(len(s)-1, -1, -1):
        answer += s[i]
    return answer

# Second
def solution2(s): 
    return ''.join(sorted(s, reverse=True))