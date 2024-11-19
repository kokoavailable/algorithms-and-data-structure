# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None  # Slow의 이전 노드를 추적
        
        # Fast 포인터가 끝에 도달할 때까지 이동
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Slow가 중간 노드를 가리키고 있으므로, 이를 제거
        prev.next = slow.next
        
        return head
        