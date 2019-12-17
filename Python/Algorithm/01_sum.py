# coding: utf-8

# 1부터 n까지의 합을 구하는 알고리즘
# 1. 합을 기록할 변수 s를 만들고 0을 저장
# 2. 변수 i를 만들어 1부터 n까지 증가시키며 반복
# 3. s에 i를 더하여 얻은 값을 다시 s에 저장
# 4. s 출력

# O(n)
def sum_n(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s

# O(1)
def sum_gaus(n):
    return n * (n + 1) // 2             # // 는 정수 나눗셈을 의미한다.

print(sum_n(10))
print(sum_n(100))
print()
print(sum_gaus(10))
print(sum_gaus(100))

# 반복문은 항상 원하는 것보다 +1
