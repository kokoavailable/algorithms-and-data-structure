# heapify 알고리즘. 최대 최소힙을 붕괴시키는 노드가 있다면, 해당 노드에 대해서 자식 노드와 자리를 바꾸고, 계속해서 이것을 반복한다.
# 한번 자식 노드로 내려갈때마다 노드의 갯수가 2배씩 증가한다는 점에서 log N의 시간 복잡도를 지닌다.

def max_heapify(arr, n, i):
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2

  if left < n and arr[left] > arr[largest]:
    largest = left

  if right < n and arr[right] > arr[largest]:
    largest = right

  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    max_heapify(arr, n, largest)

def build_max_heap(arr):
  n = len(arr)
  # 중간 이후의 노드들은 리프노드들이다.
  for i in range(n // 2 - 1, -1, -1):
    max_heapify(arr, n, i)

def heap_sort(arr):
  n = len(arr)
  build_max_heap(arr)

  # 최대힙을 빌드한 이후 가장 큰 값을 배열의 끝으로 이동시키고 남는 부분을 다시 최대 힙으로 복원하는 과정을 반복하며 오름차순 정렬한다.
  # 최소힙의 경우에는 반대.
  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    max_heapify(arr, i, 0)

# 최소힙

def min_heapify(arr, n, i):
  smallest = i
  left = 2 * i + 1
  right = 2 * i + 2

  if left < n and arr[left] < arr[smallest]:
    smallest = left

  if right < n and arr[right] < arr[smallest]:
    smallest = right

  if smallest != i:
    arr[i], arr[smallest] = arr[smallest], arr[i]
    min_heapify(arr, n, smallest)

def build_min_heap(arr):
  n = len(arr)
  for i in range(n // 2 - 1, -1, -1):
    min_heapify(arr, n, i)

def heap_sort_min(arr):
  n = len(arr)
  build_min_heap(arr)
  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    min_heapify(arr, i, 0)
