# heapq 모듈은 최소 힙을 기본으로 하며 힙생성과 요소 제거로 이루어져 있다.

# heapq.heappush(heap, item) O(log n)
# heapq.heappop(heap) O(log n) 힙에서 가장 작은 요소를 제거하고 반환한다.
# heapq.heapify(iterable) 주어진 iterable을 힙으로 변환한다. O(n)
# heapq.heappushpop(heap, item) 새로운 요소를 추가한 후 가장 작은 요소를 제거하고 반환한다. O(log n)
# heapq.nlargest(n, iterable, key=None) iterable에서 nrㅐ의 가장 큰요소들을 리스트로 반환한다.
# heapq.nsmallest(n, iterable, key=None) iterable에서 n개의 가장 작은 요소들을 리스트로 반환한다. 
