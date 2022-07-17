# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur = head
        left = None
        start = cur.next
        
        while cur and cur.next:
            
            right = cur.next
            cur.next = right.next
            right.next = cur
            if left:
                left.next = right
            left = cur
            cur = cur.next
            
        return start