# [kth_number.py]
# K번째 수

# mine
def solution1(array, commands):
    answer = []
    for command in commands:
        tmp = array[command[0]-1: command[1]]
        tmp.sort()
        answer.append(tmp[command[2]-1])
    return answer

# others
def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))