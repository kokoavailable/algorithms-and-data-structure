class Stack:
    """
    push, pop, peek, size
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    # print(stack)  출력: [1, 2, 3]
    def __str__(self):
        return str(self.items

    # print(repr(stack)) 출력 Stack([1, 2, 3])
    def __repr__(self):
        return f"Stack({self.items})"
                  
