# [madlibsgame.py]
# coding: utf-8

# 곳곳에 빠진 단어를 플레이어가 맞추는 게임

import re

text = """Giraffes have aroused
the curiosity of __PLURAL_NOUN__
since earliest times. The
giraffe is the tallest of all
living __PLURAL_NOUN__, but
scientists are unable to
explain how it got its long
__PART_OF_THE_BODY__. The
giraffe's tremendous height,
which might reach __NUMBER__
__PLURAL_NOUN__, comes from
it legs and __BODYPART__.
"""

def mad_libs(mls):
    """
    매개변수 mis: 사용자가 맞춰야 할 단어의 힌트는 밑줄 두 개 사이에 쓴다.
    힌트 사이에 밑줄 두 개가 들어가 있으면 안 된다.
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print("\n")
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid mls")

mad_libs(text)