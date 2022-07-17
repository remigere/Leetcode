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
        dummy = ListNode(-1)
        dummy.next = head
        left = dummy
        
        while cur and cur.next:
            
            right = cur.next
            
            left.next = right
            cur.next = right.next
            right.next = cur
           
            
            left = cur
            cur = cur.next
            
        return dummy.next