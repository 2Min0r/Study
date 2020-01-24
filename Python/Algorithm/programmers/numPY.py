# [numPY.py]
# 문자열 내 p와 y의 개수

# first
def solution1(s):
    answer = True
    s = s.lower()
    p = 0
    y = 0
    for i in s:
        if i == "p":
            p += 1
        if i == "y":
            y += 1
    if p != y:
        answer = False
    return answer

# second

def solution2(s):
    if s.lower().count("p") == s.lower().count("y"):
        return True
    return False