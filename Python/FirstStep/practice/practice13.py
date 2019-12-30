# [practice13.py]
# coding: utf-8

class Square():
    square_list = []
    
    def __init__(self, side):
        self.side = side
        self.square_list.append(self)
    
    def __repr__(self):
        msg = "{} by {}".format(self.side, self.side)
        return msg


square1 = Square(4)
square2 = Square(10)
square3 = Square(60)

print(square1.square_list)
