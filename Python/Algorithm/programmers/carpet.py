# [carpet.py]
# 카펫

def solution(brown, red):
    width = 0
    height = 0
    for i in range(1, red//2+1):
        width = i
        height = red//i if red%i==0 else red//i+1
        if 2*width + 2*height + 4 == brown:
            break;
    answer = [max(width, height)+2, min(width, height)+2]
    return answer