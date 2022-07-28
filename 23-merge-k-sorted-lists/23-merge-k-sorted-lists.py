# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for l in lists:
            while l:
                heapq.heappush(min_heap, l.val)
                l = l.next
        head = ListNode()
        cur = head
        while min_heap:
            cur.next = ListNode(heapq.heappop(min_heap))
            cur = cur.next
        return head.next
