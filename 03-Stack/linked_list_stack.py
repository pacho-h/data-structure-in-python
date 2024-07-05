class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if not self.is_empty():
            data = self.top.data
            self.top = self.top.next
            self.count -= 1
            return data
        raise IndexError('pop from empty stack')

    def peek(self):
        if not self.is_empty():
            return self.top.data
        raise IndexError('peek from empty stack')

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count


# 사용 예제
stack = LinkedListStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3
print(stack.peek())  # 2
print(stack.size())  # 2
print(stack.is_empty())  # False
