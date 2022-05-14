# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        prec = ListNode()
        out = ListNode()
        cur = out
        add = 0
        while n1 or n2 or add:
            cur.next = ListNode(add)
            cur = cur.next
            if n1:
                cur.val += n1.val
                n1 = n1.next
            if n2:
                cur.val += n2.val
                n2 = n2.next
            cur.val, add = cur.val % 10, cur.val // 10
        return out.next