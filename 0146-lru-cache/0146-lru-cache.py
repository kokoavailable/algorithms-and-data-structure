from collections import OrderedDict

class LRUCache:
    __slots__ = ('data', 'capacity')

    def __init__(self, capacity: int):
        self.data = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1 

        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:  # 키가 있으면
            self.data.move_to_end(key)  # 순서 업데이트
        self.data[key] = value  # 값 추가/업데이트

        if len(self.data) > self.capacity:  # 용량 초과 시 가장 오래된 항목 제거
            self.data.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)