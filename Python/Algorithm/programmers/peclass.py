# [peclass.py]
# 체육복

def solution(n, lost, reserve):
    answer = n - len(lost)
    clothes = [0]*n
    check = []
    
    for other in reserve:
        if other in lost:
            answer += 1
            check.append(other)
            continue
        clothes[other-1] = 1
            
    for i in lost:
        if i in check:
            continue
        # front
        if i-2 >= 0 and clothes[i-2] == 1:
            clothes[i-2] = 0
            answer += 1
        # back
        elif i < n and clothes[i] == 1:
            clothes[i] = 0
            answer += 1

    return answer