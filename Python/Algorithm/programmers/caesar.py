# [caesar.py]
# 시저암호

def solution(s, n):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    answer = ''

    for i in s:
        if i == " ":
            answer += i
        elif i.isupper():
            answer += alphabet[(alphabet.index(i.lower())+n) % len(alphabet)].upper()
        else:
            answer += alphabet[(alphabet.index(i.lower())+n) % len(alphabet)]
    return answer