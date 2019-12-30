# [deepoop04.py]
# coding: utf-8

# is keyword - 1
class Person():
    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)



# is keyword - 2
def find_none(x):
    if x is None:
        print("x is None")
    else:
        print("x is not None")

find_none(10)
find_none(None)