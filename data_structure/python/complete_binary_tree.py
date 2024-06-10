class CompleteBinaryTree:
  def __init__(self):
    self.tree = []

  def insert(self, key):
    self.tree.append(key)
    
  def display_tree(self):
    if not self.tree:
        print("Tree is empty")
        return

    depth = 0
    while 2 ** depth <= len(self.tree):
        depth += 1
    
    index = 0
    for level in range(depth):
        level_length = 2 ** level
        for _ in range(level_length):
            if index < len(self.tree):
                print(self.tree[index], end=' ')
                index += 1
        print()


# 50
# 30 20
# 40 70 60
