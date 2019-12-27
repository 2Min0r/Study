# [format.py]
# coding: utf-8

year = input("올해년도를 입력하세요:")
name = input("이름을 입력하세요:")
color = input("좋아하는 색을 입력하세요:")

r = "{}년도 {}씨는 {}의 빛처럼 빛나는 사람이 될 것입니다.".format(year, name, color)
print(r)