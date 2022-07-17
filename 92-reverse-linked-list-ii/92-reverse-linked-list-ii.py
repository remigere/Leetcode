# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        prev = None
        count = 0
        while m > 1:
            prev = cur
            cur = cur.next
            m -= 1
            n -= 1
        tail = cur
        con = prev
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head