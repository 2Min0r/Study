# [watermelon.py]
# 수박수박수박수박수

# first
def solution1(n):
    answer=""
    for i in range(1,n+1):
        if i%2==1:
            answer+="수"
        else:
            answer+="박"
    return answer

# second
def solution2(n):
    answer = "수박" * n//2 +1
    return answer[:n]