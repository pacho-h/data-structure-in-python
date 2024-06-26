from collections import deque


class Deque:
    def __init__(self):
        self.deque = deque()

    def append_front(self, item):
        self.deque.appendleft(item)

    def append_rear(self, item):
        self.deque.append(item)

    def pop_front(self):
        if not self.is_empty():
            return self.deque.popleft()
        raise IndexError("pop from empty deque")

    def pop_rear(self):
        if not self.is_empty():
            return self.deque.pop()
        raise IndexError("pop from empty deque")

    def front(self):
        if not self.is_empty():
            return self.deque[0]
        raise IndexError("front from empty deque")

    def rear(self):
        if not self.is_empty():
            return self.deque[-1]
        raise IndexError("rear from empty deque")

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)


# 사용 예제
dq = Deque()
dq.append_rear(1)
dq.append_rear(2)
dq.append_front(3)
print(dq.pop_front())  # 3
print(dq.pop_rear())  # 2
print(dq.front())  # 1
print(dq.rear())  # 1
print(dq.size())  # 1
print(dq.is_empty())  # False
