# [practice04.py]
# coding: utf-8

# 4-1
idol = ["트와이스", "소녀시대", "원더걸스"]
print(idol)

# 4-2
memory = [(37.2965522, 127.0134102), (37.2950174, 127.0188398), (37.3069217, 127.0134706)]
print(memory)

# 4-3
whoiam = {
    "height": 158,
    "color": "green",
    "author": "김이환"
}
print(whoiam)

# 4-4
answer = input("저의 무엇이 궁금하신가요? (height, color, author):")
if answer in whoiam:
    print(whoiam[answer])
else:
    print("준비하지 못한 내용이에요.")

# 4-5
playlist = {
    "트와이스": ["Knock Knock", "LIKEY", "TT"],
    "소녀시대": ["소녀시대", "Lion Heart", "Oh"],
    "원더걸스": ["Tell me", "Nobody"]
}
print(playlist)