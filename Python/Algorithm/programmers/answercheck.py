# [answercheck.py]
# 모의고사

def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5] * (len(answers)//5+1)
    student1 = student1[:len(answers)]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8+1)
    student2 = student2[:len(answers)]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10+1)
    student3 = student3[:len(answers)]
    score = [0, 0, 0]
    for a, b, c, ans in zip(student1, student2, student3, answers):
        if a == ans:
            score[0] += 1
        if b == ans:
            score[1] += 1
        if c == ans:
            score[2] += 1

    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)

    return answer