# 구현

class Queue:
  """
  선입선출을 따르는 자료구조로 먼저 추가된 요소가 제거가 된다.
  """
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def enqueue(self, item):
    self.items.append(item)

  #시간 복잡도 O(n)
  def dequeue(self):
    if self.is_empty():
      raise IndexError("dequeue from empty queue")
    return self.items.pop(0)

  def peek(self):
    if self.is_empty():
      raise IndexError("peek from empty queue")
    return self.items[0]

  def size(self):
    return len(self.items)

  def __str__(self):
    return str(self.items)

  def __repr__(self):
      return f"Queue({self.items})"

# 내부 라이브러리로서의 queue

# 주로 멀티스레딩 환경에서 사용되기 위해 설계된 큐이며, 동기화 매커니즘을 제공한다. 
# 내부적으로 락 매커니즘을 사용한다. 파이썬 표준라이브러리의 일부이며 CPython으로 구현 돼 있다.

# 주요 메서드

# 선언. maxsize 를 인자로 받는다.

# put(item, block=True, timeout=None) 큐에 아이템을 추가한다. block이 true라면 큐가 가득 찬경우 대기, false인 경우 예외를 발생시킨다.
# timeout 대기시간을 지정하며 none일 경우 무한정 대기한다.

# get(block=True, timeout=None) 큐에 아이템을 제거하고 반환한다.
# block이 true일 경우 큐가 비어있는 경우 대기하며, false일 경우 큐가 비어 있으면 queue.Empty 예외를 발생시킨다.

# qsize() 큐크기를 반환한다. 현재 큐에 있는 아이템의 개수를 반환한다.

# empty() 큐가 비어있는지 확인한다. 큐가 비어있으면 True, 그렇지 않으면 False

# full() 큐가 가득 찼는지 확인하며, 가득 차 있으면 True, 그렇지 않으면 False

# task_done() get 메서드로 가져온 작업이 완료 됐음을 큐에 얼린다. 
# join 메소드와 함꼐 사용한다면 task_done메서드의 호출수가 큐에 추가된 작업의 수가 동일해질 떄까지 대기한다.

# 큐를 활용한 멀티 스레딩

import queue
import threading

# 큐 생성
q = queue.Queue()

# 작업을 수행하는 스레드 함수
def worker():
    while True:
        item = q.get()
        if item is None:  # 작업 종료를 알리는 신호
            break
        print(f"Working on {item}")
        q.task_done()  # 작업 완료를 알림

# 스레드 생성
thread = threading.Thread(target=worker)
thread.start()

# 큐에 작업 추가
for item in range(10):
    q.put(item)

# 모든 작업이 완료될 때까지 대기
q.join()  # 큐에 추가된 모든 작업이 완료될 때까지 대기

print("All work completed")

# 작업 종료를 알리기 위해 None을 큐에 추가
q.put(None)
thread.join()
