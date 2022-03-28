# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        if not(l1):
            return l2
        if not l2:
            return l1
        n1 = l1
        s = n1.val
        count = 0
        while n1.next:
            count += 1
            n1 = n1.next
            s += n1.val * (10) ** (count)
        n2 = l2
        s += n2.val
        count = 0
        while n2.next:
            count += 1
            n2 = n2.next
            s += n2.val * (10) ** (count)
        prec = None
        for char in str(s):
            cur = ListNode(int(char), prec)
            prec = cur
        return cur
        """
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next