# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = ListNode()
        m.next = head
        curr = m
        prev = m
        step = 0
        while step < n+1:
            prev = prev.next
            step += 1
        while prev:
            prev = prev.next
            curr = curr.next
        curr.next = curr.next.next
        return m.next

        