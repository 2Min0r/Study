# [gcdlcm.py]
# 최대공약수와 최소공배수

def solution(n, m):
    answer = [1, n*m]
    # 최대공약수
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer[0] = i
            break
    # 최소공배수
    for i in range(max(n,m), n*m +1):
        if i % n == 0 and i % m == 0:
            answer[1] = i
            break
    return answer