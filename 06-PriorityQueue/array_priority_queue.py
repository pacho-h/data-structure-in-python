class ArrayPriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort(reverse=True)

    def extract_max(self):
        if not self.is_empty():
            return self.queue.pop(0)[1]
        raise IndexError('extract_max from empty queue')

    def peek(self):
        if not self.is_empty():
            return self.queue[0][1]
        raise IndexError('peek from empty queue')

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# 사용 예제
apq = ArrayPriorityQueue()
apq.insert('task1', 1)
apq.insert('task2', 3)
apq.insert('task3', 2)
print(apq.extract_max())  # task2
print(apq.peek())  # task3
print(apq.size())  # 2
print(apq.is_empty())  # False
