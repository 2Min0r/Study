# [oop01.py]
# coding: utf-8

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
    
    def change_data(self, index, n):
        self.nums[index] = n
    
# Data 객체를 통해 인스턴스 변수 nums에 직접 접근
data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

# change_data 메서드 사용
data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)