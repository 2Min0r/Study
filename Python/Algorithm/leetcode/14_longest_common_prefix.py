# [14_longest_common_prefix.py]

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        shortest = min(strs, key=len)
        for i, string in enumerate(shortest):
            for j in strs:
                if j[i] != string:
                    return shortest[:i]
        
        return shortest