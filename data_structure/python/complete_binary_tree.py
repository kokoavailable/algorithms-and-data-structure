class CompleteBinaryTree:
  def __init__(self):
    self.tree = []

  def insert(self, key):
    self.tree.append(key)
    self.heapify_up(len(self.tree) -1)

  def heapify_up(self, index):
    parent_index = (index - 1) // 2
    
