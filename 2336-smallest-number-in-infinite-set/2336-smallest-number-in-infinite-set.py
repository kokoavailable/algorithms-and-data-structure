class SmallestInfiniteSet:

    def __init__(self):
        self.current_min = 1
        self.removed_set = set()
        self.min_heap = []

    def popSmallest(self) -> int:
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)
            self.removed_set.remove(smallest)
            return smallest

        self.current_min += 1
        return self.current_min - 1

    def addBack(self, num: int) -> None:
        if num < self.current_min and num not in self.removed_set:
            heapq.heappush(self.min_heap, num)
            self.removed_set.add(num)    


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)