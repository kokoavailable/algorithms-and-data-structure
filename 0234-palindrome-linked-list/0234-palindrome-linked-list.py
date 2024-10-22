# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
            
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True

#    def isPalindrome(head: ListNode) -> bool:
#     vals = []
    
#     # 1. 연결 리스트를 순회하면서 값들을 배열에 저장
#     current = head
#     while current:
#         vals.append(current.val)
#         current = current.next
    
#     # 2. 배열을 이용해 회문 여부를 확인
#     return vals == vals[::-1]