# [deepoop02.py]
# coding: utf-8

class Lion():
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)                     # 메모리상의 주소가 아닌 name 출력