# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_less = ListNode(0)
        less_curr = dummy_less
        dummy_more = ListNode(0)
        more_curr = dummy_more
        curr = head

        while curr:
            if curr.val < x:
                less_curr.next = curr
                less_curr = less_curr.next
            else:
                more_curr.next = curr
                more_curr = more_curr.next

            curr = curr.next

        more_curr.next = None

        less_curr.next = dummy_more.next
        return dummy_less.next

        