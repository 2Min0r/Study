# [2016.py]
# 2016년

# First time
def solution1(a, b):
    answer = ''
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    total = 0
    for i in range(1, a):
        total += days[i]
    total += b
    answer = week[total % 7]
    return answer

# Improve
def solution2(a, b):
    answer = ''
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    answer = week[(sum(days[:a]) + b) % 7]
    return answer