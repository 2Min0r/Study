# [09_palindrome_number.py]

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x[::-1] != x:
            return False
        else:
            return True