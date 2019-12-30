# [practice03.py]
# coding: utf-8

# 3 - 1
def sqr(a):
    """
    Take an int and return it multiplied by 2.
    :param a: int.
    :return: x multiplied by 2.
    """
    return a * a

# 3 - 2
def print_str(a):
    """
    Prints the string passed in.
    :param a: str.
    """
    return print(a)

# 3 - 3
def five_var(a, b, c, d = 4, e = 5):
    """
    Return the result of addition of 5 params with 2 optional params
    :param a: int.
    :param b: int.
    :param c: int.
    :param d: int.
    :param e: int.
    :return: int.
    """
    return a + b + c + d + e

# 3 - 4
def div2(a):
    """
    Takes an int and returns it divided by 2.
    :param a: int.
    :return: a divided by 2.
    """
    return a // 2

def multi(a):
    """
    Takes an int and return it multiplied by 4.
    :param a: int.
    :return: a multiplied by 4.
    """
    return a * 4

x = div2(10)
print(multi(x))

# 3 - 5
def change_float(a):
    """
    Convert passed in str to int.
    :param a: str.
    :return: string converted to float.
    """
    try:
        return float(a)
    except ValueError:
        return print("Invalid parameter")