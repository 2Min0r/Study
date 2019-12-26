# [exceptionhandling.py]
# coding: utf-8


try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a / b)

except(ZeroDivisionError, ValueError):
    print("Invalid input.")