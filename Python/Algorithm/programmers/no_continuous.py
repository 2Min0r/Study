# [no_continuous.py]
# 같은 숫자는 싫어

# First code
def solution1(arr):
    answer = [arr[0]]
    j = 0
    for item in arr:
        if item != answer[j]:
            answer.append(item)
            j += 1
    return answer

# Improved code
def solution2(arr):
    answer = [arr[0]]
    for item in arr:
        if item != answer[-1]:
            answer.append(item)
    return answer
