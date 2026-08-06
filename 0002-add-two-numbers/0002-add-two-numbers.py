# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #leetcode
        def toNumber(node):
            num = 0
            place = 1
            while node:
                num += node.val * place
                place *= 10
                node = node.next
            return num

        total = toNumber(l1) + toNumber(l2)

        dummy = ListNode(0)
        curr = dummy

        if total == 0:
            return ListNode(0)

        while total > 0:
            curr.next = ListNode(total % 10)
            curr = curr.next
            total //= 10

        return dummy.next