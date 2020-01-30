# [to_weird_case.py]
# 이상한 문자 만들기

# first
def solution1(s):
    s = s.split(" ")
    answer = []
    for i in s:
        tmp = list(i)
        for j in range(0, len(tmp)):
            if (j+1) % 2 == 1:
                tmp[j] = tmp[j].upper()
            else:
                tmp[j] = tmp[j].lower()
        tmp = "".join(tmp)
        answer.append(tmp)
    return " ".join(answer)