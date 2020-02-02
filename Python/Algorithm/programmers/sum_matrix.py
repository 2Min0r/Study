# [sum_matrix.py]
# 행렬의 덧셈

# first
def solution1(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        tmp = []
        for j in range(0, len(arr1[i])):
            tmp.append(arr1[i][j]+arr2[i][j])
        answer.append(tmp)
    return answer

# second
def solution2(arr1, arr2):
    for i in range(0, len(arr1)):
        for j in range(0, len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1