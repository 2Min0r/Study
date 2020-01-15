# [11_container_with_most_water.py]

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head = 0
        tail = len(height) - 1
        maxarea = 0
        for i in range(0, len(height)):
            width = abs(head - tail)
            if height[head] < height[tail]:
                tmp = width * height[head]
                head += 1
            else:
                tmp = width * height[tail]
                tail -= 1
            if tmp > maxarea:
                maxarea = tmp
        return maxarea