# coding: utf-8

def getname(s_no, s_name, find_no):
    n = len(s_no)
    for i in range(0, n):
        if s_no[i] == find_no:
            return s_name[i]
    return str("?")

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(getname(stu_no, stu_name, 11))
print(getname(stu_no, stu_name, 105))