# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        res = ListNode()
        cur = res
        while head and head.next:
            #print(cur, head, head.next)
            cur.next = ListNode(head.next.val, ListNode(head.val))
            head = head.next.next
            cur = cur.next.next
        if head:
            cur.next = head
        return res.next
            