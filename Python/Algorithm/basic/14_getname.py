# coding: utf-8

def getname(stu, no):
    if no in stu:
        return stu[no]
    
    return "?"



student = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}
print(getname(student, 39))
print(getname(student, 11))