# [paradaim02.py]
# coding: utf-8

class Orange:
    def __init__(self, w, c):
        """무게는 온스(oz) 단위"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")
    
    def rot(self, days, temp):
        """
        days: 구매후 날짜
        temp: 구매후의 평균기온
        """
        self.mold = days * temp

orange = Orange(6, "ornage")
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)