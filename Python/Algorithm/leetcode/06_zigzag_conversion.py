# [06_zigzag_conversion.py]

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # numRows 수만큼 배열 크기 생성
        zigzag = [""] * numRows

        result = ""
        # zigzag의 인덱스
        count = 0

        flag = 1

        if numRows == 1:
            return s
        
        for i, char in enumerate(s):
            zigzag[count] += char

            count += flag
            if count == 0 or count == numRows - 1:
                flag *= (-1)

        for i in range(1, numRows):
            result = result + zigzag[i]
        result = zigzag[0] + result

        return result