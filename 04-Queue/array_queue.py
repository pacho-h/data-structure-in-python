class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError('dequeue from empty queue')

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError('front from empty queue')

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# 사용 예제
queue = ArrayQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 1
print(queue.front())  # 2
print(queue.size())  # 2
print(queue.is_empty())  # False
