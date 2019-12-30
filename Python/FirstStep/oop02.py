# [oop02.py]
# coding: utf-8

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # 이 코드는 클라이언트에서 사용 가능
        pass

    def _unsafe_method(self):
        # 이 코드는 클라이언트에서 사용 불가능
        pass
