class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front_node = None
        self.rear = None
        self.count = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front_node = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.count += 1

    def dequeue(self):
        if not self.is_empty():
            data = self.front_node.data
            self.front_node = self.front_node.next
            self.count -= 1
            if self.front_node is None:
                self.rear = None
            return data
        raise IndexError("dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.front_node.data
        raise IndexError("front from empty queue")

    def is_empty(self):
        return self.front_node is None

    def size(self):
        return self.count


# 사용 예제
queue = LinkedListQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 1
print(queue.front())  # 2
print(queue.size())  # 2
print(queue.is_empty())  # False
