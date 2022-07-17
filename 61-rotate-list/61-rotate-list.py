# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        n = 1
        while cur.next:
            n += 1
            cur = cur.next
        r = (n - k) % n
        print(r)
        if r == 0:
            return head
        cur = head
        flag = True
        while r > 1:
            cur = cur.next
            r -= 1
        lB = cur.next
        cur.next = None
        cur = lB
        while cur.next:
            cur = cur.next
        cur.next = head
        return lB
            