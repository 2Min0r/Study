# [practice20.py]
# coding: utf-8

# 20-1
class Stack():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


stack1 = Stack()
l = "yesterday"

for i in l:
    stack1.push(i)

for i in range(stack1.size()):
    print(stack1.pop(), end="")

print()
# 20-2
list1 = [1, 2, 3, 4, 5]
list2 = []

stack2 = Stack()

for i in list1:
    stack2.push(i)

for i in range(stack2.size()):
    list2.append(stack2.pop())

print(list2)