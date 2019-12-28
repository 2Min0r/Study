# [compare.py]
# coding: utf-8
# 샘플코드와 직접만든코드 속도 비교(샘플코드 < 직접만든코드) 이겼다!

import time
import random

def hangman_sample(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You lose! It was {}."
              .format(word))


def hangman_my(word):
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



def test():
    a = "cat"

    # max_profit_fast Algorithm test
    start = time.time()
    mpf = hangman_my(a)
    end = time.time()
    time_fast = end - start

    # hangman_sample Algorithm test
    start = time.time()
    mps = hangman_sample(a)
    end = time.time()
    time_slow = end - start


    # result
    print(mps, mpf)
    m = 0
    if time_fast > 0:
        m = time_slow / time_fast
    print("%.5f %.5f %.2f" % (time_slow, time_fast, m))

test()