class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError('pop from empty stack')

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError('peek from empty stack')

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# 사용 예제
stack = ArrayStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3
print(stack.peek())  # 2
print(stack.size())  # 2
print(stack.is_empty())  # False
