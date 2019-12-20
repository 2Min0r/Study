# coding: utf-8

# 얄팍한 코딩사전 자바스크립트 언어로 표기된 것, 파이썬 변환
# recursive 원리 이해할 수 있는 함수

def recursive_sum(sum, a):
    n = len(a)
    if n <= 0:
        print("총합은", sum)
        return sum
    else:
        print("recursive_sum(", sum, a, ")가")
        return recursive_sum(sum + a.pop(0), a)
    print("이라고 말했어요.")


d = [3, 1, 4, 1, 5, 9]
recursive_sum(0, d)
