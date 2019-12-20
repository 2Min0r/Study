# coding: utf-8

# 얄팍한 코딩사전의 리스트 안의 리스트의 합까지 구하는 자바스크립트 프로그램을 파이썬 프로그램으로 바꿈

def recursive_sum(sum, a):
    n = len(a)
    if n <= 0:
        return sum
    else:
        value = a[0]
        del(a[0])

        if value == int:
            print("recursive_sum(", sum, "+", value, a, ")")
            return recursive_sum(sum + value, a)
        else:
            print("recursive_sum(", sum , "+", value, a, ")")
            return recursive_sum(sum + value if type(value) == int else recursive_sum(sum, value), a)
            

d = [[1,2], 3, 4, [5,[10, [1, 2]], 6], 7, 8, [9, 10]]
print("총합 =", recursive_sum(0, d))