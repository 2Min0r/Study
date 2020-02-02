# [rectangle_star.py]
# 직사각형 별찍기

# first
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print("*",end='')
    print()

# second
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*" * a)

# third
a, b = map(int, input().strip().split(' '))
print(("*" * a + "\n") * b)