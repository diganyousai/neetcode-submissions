# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#三个重点需要改的连接点：1.tail连到开头  2.前半段连到None   3.建立新的newHead
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        length, tail = 1, head
        while tail.next:     #找到tail
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head       #全程不要动head,直接连过来就行了

        return newHead