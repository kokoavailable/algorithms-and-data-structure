class ListNode:
  def __init__(self, data=0, next=None):
    self.data = data
    self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
      """
      O(n)
      """
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
      """
      O(n) 노드가 주어졌을떄
      """
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
      """
      O(n) 노드가 주어졌을떄
      """
        current = self.head
        while current and current.data != key:
            current = current.next
        return current

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
