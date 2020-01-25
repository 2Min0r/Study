# [alpha_string46.py]
# 문자열 다루기 기본

# First
def solution1(s):
    try : 
        int(s)
        if len(s) == 4 or len(s) == 6 :
            return True 
        else:  
            return False
    except :
        return False

# Second
def solution2(s):
    return s.isdigit() and len(s) in (4, 6)