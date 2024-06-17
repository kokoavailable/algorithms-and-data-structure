# 트라이
# 문자열 집합을 저장하고 빠르게 검색하는데 사용된다. 특히 문자열 탐색과 관련된 많은 문제에서 유용하다.

class TrieNode:
  """
  Node, Edge, Root 로 이루어지며 각 노드는 여러 자식을 가질 수 있다, 그리고 특정 노드가 단어의 끝인지 표시하는 방법을 불리언 값으로 표시한다.
  """
  def __init__(self):
    self.children = {}
    self.is_end_of_word = False

class Trie:
  def __init__(self):
      self.root = TrieNode()

  def insert(self, word):
    """
    한글자씩 트라이에 추가한다. 각 글자는 현재 노드에서 시작해 자식 노드로 이동하며 추가되고, 단어의 마지막 글자에 도달하면 단어의 끝을 표시한다.
    """
    node = self.root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True

  def search(self, word):
    """
    특정 단어가 트라이에 존재하는지 확인한다.
    루트에서 시작해 각 글자에 대해 자식 노드로 이동한다.
    단어의 끝에 도달했을 때 단어의 끝 표시가 있는지 확인한다.
    """
    node = self.root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end_of_word

  def starts_with(self, prefix):
    """
    특정 접두사로 시작하는 단어가 트라이에 존재하는가 ?
    """
    node = self.root
    for char in prefix:
        if char not in node.children:
            return False
        node = node.children[char]
    return True
