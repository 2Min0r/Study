# [add_two_numbers.py]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = result = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            tmp1 = l1.val if l1 else 0
            tmp2 = l2.val if l2 else 0
            totalSum = tmp1 + tmp2 + carry
            
            result.next = ListNode(totalSum % 10)
            result = result.next
            carry = totalSum // 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return head.next
    