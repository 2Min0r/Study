# [algorithm02.py]
# coding: utf-8

def ss(number_list, n):
    for i in number_list:
        if i == n:
            return True
    return False


numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)