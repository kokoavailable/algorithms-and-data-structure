# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 길이를 계산하는 함수
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        # 두 리스트를 동일한 길이로 패딩하는 함수
        def pad_list(l, pad_length):
            for _ in range(pad_length):
                new_node = ListNode(0)
                new_node.next = l
                l = new_node
            return l

        # 재귀적으로 합산하는 함수
        def add_nodes(l1, l2):
            # 종료 조건: 두 리스트가 모두 None이면 0을 반환
            if not l1 and not l2:
                return None, 0
            
            # 재귀적으로 다음 노드를 처리
            next_node, carry = add_nodes(l1.next if l1 else None, 
                                         l2.next if l2 else None)
            
            # 현재 자리 계산
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current_node = ListNode(total % 10)
            current_node.next = next_node
            
            return current_node, carry
        
        # 리스트의 길이를 맞추기
        len1, len2 = get_length(l1), get_length(l2)
        if len1 < len2:
            l1 = pad_list(l1, len2 - len1)
        else:
            l2 = pad_list(l2, len1 - len2)
        
        # 재귀 호출로 합산
        result, carry = add_nodes(l1, l2)
        
        # 최종 캐리를 처리
        if carry:
            new_node = ListNode(carry)
            new_node.next = result
            result = new_node
        
        return result