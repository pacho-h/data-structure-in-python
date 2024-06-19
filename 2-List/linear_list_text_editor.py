class TextNode:
    def __init__(self, char):
        self.char = char
        self.next = None


class TextEditor:
    def __init__(self):
        self.head = None

    def insert(self, char, position):
        new_node = TextNode(char)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next:
                    current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next:
                    current = current.next
            if current.next:
                current.next = current.next.next

    def display(self):
        current = self.head
        text = ''
        while current:
            text += current.char
            current = current.next
        print(text)


# 1. 초기 테스트: 'Hello World!'
editor = TextEditor()
editor.insert('H', 0)
editor.insert('e', 1)
editor.insert('l', 2)
editor.insert('l', 3)
editor.insert('o', 4)
editor.insert(' ', 5)
editor.insert('W', 6)
editor.insert('o', 7)
editor.insert('r', 8)
editor.insert('l', 9)
editor.insert('d', 10)
editor.insert('!', 11)
editor.display()  # Hello World!

# 2. 'Hello World!'에서 'l' 삭제
editor.delete(3)
editor.display()  # Helo World!

# 3. 'Helo World!'에서 ' ' 삭제
editor.delete(4)
editor.display()  # HeloWorld!

# 4. HeloWorld!'에서 'e' 삭제
editor.delete(1)
editor.display()  # HloWorld!

# 5. 'HloWorld!'에서 'H' 삭제
editor.delete(0)
editor.display()  # loWorld!
