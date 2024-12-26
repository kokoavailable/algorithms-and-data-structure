# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: 'Optional[ListNode]', left: int, right: int) -> 'Optional[ListNode]':
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        start = prev.next
        
        for _ in range(right - left):
            then = start.next
            start.next, then.next, prev.next = then.next, prev.next, then
        
        return dummy.next