# [practice06.py]
# coding: utf-8

# 6-1
dramas = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for drama in dramas:
    print(drama)

print()

# 6-2
for i in range(25, 50 + 1):
    print(i)

print()

# 6-3
for i, drama in enumerate(dramas):
    print(i, drama)

print()

# 6-4
numbers = [11, 22, 33, 4, 52, 16, 57, 8]
while True:
    find = input("Guess a number or type q to quit.:")
    if find == "q":
        break
    try:
        find = int(find)
    except ValueError:
        print("please type a number or q to quit.")
    if find in numbers:
        print("YES! It is in the list")
    else:
        print("NO. It is not in the list")
    
# 6-5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
result = []

for i in list1:
    for j in list2:
        result.append(i*j)
print(result)
