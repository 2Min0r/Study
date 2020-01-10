# [08_string_to_integer(atoi).py]

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        sign = 1
        tmp = ["0"]
        
        s = s.strip()
        if len(s) > 1:
            if s[0] == "-":
                sign = -1
                s = s[1:]
            elif s[0] == "+":
                sign = 1
                s = s[1:]
        elif len(s) == 0:
            return 0

        if not s[0].isdigit():
            return 0
        
        for i in s:
            if i.isdigit():
                tmp[0] = tmp[0] + i
            else:
                break
        result = int(tmp[0]) * sign
        
        if result < -2**31:
            return -2**31
        elif result >= 2**31:
            return 2**31-1
        else:
            return result