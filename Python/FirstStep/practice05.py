# [practice05.py]
# coding: utf-8

# 5-1
print("Camus")

# 5-2
print("Yesterday I wrote a {}.".format(input("어제 쓴 것:")))
print("I sent it to {}!".format(input("어제 보낸 것:")))

# 5-3
print("aldous Huxley was born in 1894".capitalize())

# 5-4
print("Where now? Who now? When now?".split("? "))

# 5-5
sentence = ["The", "fox", "jumped", "over", "the", "fence", "."]
sentence = " ".join(sentence)
sentence = sentence[0:-2] + "."
print(sentence)

# 5-6
print("A screaming comes across the sky.".replace("s", "$"))

# 5-7
print("Hemingway".index("m"))

# 5-8
print("성공의 80%는 \"자신감\"에 달려있지")

# 5-9
a = "three"
print(a + a + a)
print(a * 3)

# 5-10
april = "It was a bright cold day in April, and the clocks were striking thirteen."
print(april[0:33])