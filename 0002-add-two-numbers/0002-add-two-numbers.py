# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        def listnode(check1, check2, carry):
            if not check1 and not check2 and carry == 0:
                return None

            val1 = check1.val if check1 else 0
            val2 = check2.val if check2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            current_node = ListNode(total % 10)

            next1 = check1.next if check1 else None
            next2 = check2.next if check2 else None
            current_node.next = listnode(next1, next2, carry)

            return current_node  # 현재 노드 반환
        
        return listnode(l1, l2, 0)
    