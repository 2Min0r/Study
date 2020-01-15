# [13_roman_to_integer.py]

# mine
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        
        result = 0
        s_idx = 0
        sym_idx = len(symbols) - 1
        
        while s_idx < len(s) and sym_idx < len(symbols):
            if sym_idx-1 >= 0 and s_idx+1 < len(s) and symbols[sym_idx][0] == s[s_idx] + s[s_idx+1]:
                result += symbols[sym_idx][1]
                s_idx += 2
            elif symbols[sym_idx][0] == s[s_idx]:
                result += symbols[sym_idx][1]
                s_idx += 1
            else:
                sym_idx -= 1

        return result

# not mine
class Solution2(object):
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number