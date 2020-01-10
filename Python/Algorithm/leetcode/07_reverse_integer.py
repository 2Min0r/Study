# [07_reverse_integer.py]

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        result = str(x)
        
        if len(result) == 1:
            return x
        
        if result[0] == "-":
            result = result[0] + result[1:][::-1]
        elif result[0] == "0":
            result = result[1:][::-1]
        else:
            result = result[::-1]
        
        return int(result) if -2**31 <= int(result) < 2**31 else 0