# [harshad.py]
# 하샤드 수

# first
def solution1(x):
    return True if x % sum([int(v) for v in str(x)]) == 0 else False

# second
def solution2(x):
    return x % sum([int(v) for v in str(x)]) == 0