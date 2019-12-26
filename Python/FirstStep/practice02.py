# [practice02.py]
# coding: utf-8

# 2 - 1
print("a", "b", "c")

# 2 - 2
x = 10
if x < 10:
    print("변수는 10보다 작습니다.")
else:
    print("변수는 10보다 크거나 같습니다.")

# 2 - 3
y = 10
if y <= 10:
    print("변수는 10보다 작거나 같습니다.")
elif y <= 25:
    print("변수는 10보다 크지만 25보다 작거나 같습니다.")
else:
    print("변수는 25보다 큽니다.")

# 2 - 4
a = 7
b = 2

def remainder(a, b):
    print(a, "에서", b, "를 나눈 나머지는", a % b)

remainder(a, b)

# 2 - 5
def quotient(a, b):
    print(a, "에서", b, "를 나눈 몫은", a // b)

quotient(a, b)

# 2 - 6
age = 21
if age < 19:
    print("청소년입니다. 주류를 구매할 수 없습니다.")
else:
    print("성인입니다. 주류를 구매할 수 있습니다.")