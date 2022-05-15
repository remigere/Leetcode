# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        count = 0
        while count < n:
            count += 1
            first = first.next
        print(first)
        if not first:
            return head.next
        prec = first
        while first:
            first = first.next
            prec = second
            second = second.next
        prec.next = prec.next.next
        return head