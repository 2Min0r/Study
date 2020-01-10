# [03_longest_substring_without_repeating_characters.py]

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ""
        maxLength = 0
        
        for char in s:
            if char not in sub:
                sub += char
                maxLength = max(maxLength, len(sub))
            else:
                cut = sub.index(char)
                sub = sub[cut+1:] + char
        return maxLength