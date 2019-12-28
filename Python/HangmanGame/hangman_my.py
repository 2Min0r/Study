# [hangman_my.py]
# coding: utf-8
# 문제 보고 직접 만든 코드 

def hangman(word):
    rletters = list(word)
    n = len(rletters)
    wrong = 0
    board = ["_"] * n
    stages = ["",
    "__________          ",
    "|         |         ",
    "|         |         ",
    "|         O         ",
    "|        /|＼        ",
    "|        /＼        ",
    "|                   "]
    # 게임 시작
    print("Welcome to Hangman")
    while wrong <= len(stages) - 1:
        guess = input("Guess a letter:")

        # 글자를 맞추지 못했을 경우
        if guess not in rletters:
            wrong += 1
            for i in range(0, wrong):
                print(stages[i])

        # 글자를 맞추었을 경우
        while guess in rletters:
            cidx = rletters.index(guess)
            board[cidx] = guess
            rletters[cidx] = "$"

            # 단어를 맞추었을 경우(성공)
            if "_" not in board:
                print("You win! It was {}".format(board))
                return

        # 맞춰야 할 단어 표시
        for b in board:
            print(b, end = " ")
        print()
    
    # 단어를 맞추지 못했을 경우(실패)
    if wrong == len(stages):
        print("You lose! It was {}.".format(word))

hangman("cat")