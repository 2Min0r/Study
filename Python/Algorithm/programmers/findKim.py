# [findKim.py]
# 서울에서 김서방 찾기

# First
def solution1(seoul):
    return "김서방은 "+str(seoul.index("Kim"))+"에 있다"

# Second
def solution2(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))

# Third
def solution3(seoul):
    return ("김서방은 %d에 있다" %seoul.index("Kim"))

