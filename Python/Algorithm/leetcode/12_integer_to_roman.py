# [12_integer_to_roman.py]

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbols = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        
        result = ""
        for i in range(len(symbols) -1, -1, -1):
            result += (num // symbols[i][1]) * symbols[i][0]
            num -= num // symbols[i][1] * symbols[i][1]

        return result
    
