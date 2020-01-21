# [compress.py]
# 문자열 압축

def solution(s):
    answer = 0
    cut = 1
    if len(s) < 2:
        return len(s)
    
    while cut <= len(s) // 2:
        times = 1
        answers = ""
        char = ""
        i = 0
        while i < len(s):
            char = s[i:i+cut]
            if char == s[i+cut:i+cut+cut]:
                times += 1
            else:
                if times != 1:
                    answers += str(times)+char
                    times = 1
                else:
                    answers += char
            i = i+cut
        cut += 1
        if answer == 0 or answer > len(answers):
            answer = len(answers)
    return answer