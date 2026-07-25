# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        result=result[::-1]
        c=head
        m=head    
        i=0   
        while c is not None:
            c.val=result[i]
            c=c.next
            i+=1
        return m
 


        