# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # min_heap = []
        # for l in lists:
        #     while l:
        #         heapq.heappush(min_heap, l.val)
        #         l = l.next
        # head = ListNode()
        # cur = head
        # while min_heap:
        #     cur.next = ListNode(heapq.heappop(min_heap))
        #     cur = cur.next
        # return head.next
        
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
        head = ListNode()
        cur = head
        while min_heap:
            val, i = heapq.heappop(min_heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next