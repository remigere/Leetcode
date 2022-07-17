# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        start_odd = head
        start_even = head.next
        
        odd = start_odd
        even = start_even
        
        while odd and even:
            odd.next = even.next
            prev = odd
            odd = odd.next
            if odd:
                even.next = odd.next
            else:
                even.next = None
            even = even.next
        
        if odd:
            odd.next = start_even
        else:
            prev.next = start_even
        
        return start_odd