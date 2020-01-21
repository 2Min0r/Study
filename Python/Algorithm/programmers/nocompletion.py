# [nocompletion.py]
# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i, j in zip(participant, completion+[""]):
        if i != j:
            answer = i
            break

    return answer