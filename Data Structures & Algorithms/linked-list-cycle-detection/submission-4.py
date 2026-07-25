# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = head
        curr = head
        while prev and curr:
            if prev.next == curr:
                return True
            if prev.next is None:
                return False
            prev = prev.next.next
            curr = curr.next
        if prev is None:
            return False 
        