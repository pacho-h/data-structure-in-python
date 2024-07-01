class Node:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None


class LinkedListPriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, item, priority):
        new_node = Node(item, priority)
        if self.head is None or self.head.priority < priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def extract_max(self):
        if not self.is_empty():
            item = self.head.item
            self.head = self.head.next
            return item
        raise IndexError('extract_max from empty queue')

    def peek(self):
        if not self.is_empty():
            return self.head.item
        raise IndexError('peek from empty queue')

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


# 사용 예제
llpq = LinkedListPriorityQueue()
llpq.insert('task1', 1)
llpq.insert('task2', 3)
llpq.insert('task3', 2)
print(llpq.extract_max())  # task2
print(llpq.peek())  # task3
print(llpq.size())  # 2
print(llpq.is_empty())  # False
