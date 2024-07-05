import heapq


class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, item, priority):
        heapq.heappush(self.heap, (-priority, item))

    def extract_max(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]
        raise IndexError('extract_max from empty queue')

    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]
        raise IndexError('peek from empty queue')

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


# 사용 예제
hpq = HeapPriorityQueue()
hpq.insert('task1', 1)
hpq.insert('task2', 3)
hpq.insert('task3', 2)
print(hpq.extract_max())  # task2
print(hpq.peek())  # task3
print(hpq.size())  # 2
print(hpq.is_empty())  # False
