
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next =None
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) ->ListNode:
        result = ListNode(0)
        curr= 0
        carry = 0
        while l1 or l2:
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                pass
            curr = l1.val + l2.val + carry
            result.val = curr%10
            carry = curr//10
