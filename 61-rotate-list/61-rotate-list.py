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
        cur.next = head
        
        r = n - k % n

        new_tail = head
        while r > 1:
            new_tail = new_tail.next
            r -= 1
        new_head = new_tail.next
        new_tail.next = None
        return new_head
            