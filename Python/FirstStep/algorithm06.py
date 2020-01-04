# [algorithm06.py]
# coding: utf-8

def bottles_of_beer(bob):
    """ 99 Bottle of Beer on the Wall의 가사를 출력한다.
    매개 변수 bob은 반드시 양의 정수여야 한다.
    """
    if bob < 1:
        print(""" 
        No more bottles of beer on the wall. No more bottles of beer.
        """)
        return                                                              # 첫번째 원칙
    tmp = bob
    bob -= 1                                                                # 두번째 원칙
    print("""
    {} bottles of beer on the wall. {} bottles of beer.
    Take one down, pass it around, {} bottles of beer on the wall.
    """.format(tmp, tmp, bob))
    bottles_of_beer(bob)                                                    # 마지막 원칙

bottles_of_beer(99)