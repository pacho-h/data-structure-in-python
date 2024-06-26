class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class DictionaryBST:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if self.root is None:
            self.root = BSTNode(word)
        else:
            self._insert(self.root, word)

    def _insert(self, current, word):
        if word < current.value:
            if current.left is None:
                current.left = BSTNode(word)
            else:
                self._insert(current.left, word)
        else:
            if current.right is None:
                current.right = BSTNode(word)
            else:
                self._insert(current.right, word)

    def search(self, word):
        return self._search(self.root, word)

    def _search(self, current, word):
        if current is None or current.value == word:
            return current

        if word < current.value:
            return self._search(current.left, word)

        return self._search(current.right, word)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)


# 사용 예제
dictionary = DictionaryBST()
dictionary.insert('apple')
dictionary.insert('banana')
dictionary.insert('cherry')
dictionary.insert('date')
dictionary.insert('fig')
dictionary.insert('grape')
dictionary.inorder_traversal(dictionary.root)  # apple banana cherry date fig grape
print(dictionary.search('cherry') is not None)  # True
print(dictionary.search('kiwi') is not None)  # False
