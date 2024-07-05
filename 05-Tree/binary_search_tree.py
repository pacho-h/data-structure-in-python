class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.value:
            if current.left is None:
                current.left = BSTNode(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = BSTNode(key)
            else:
                self._insert(current.right, key)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None or current.value == key:
            return current

        if key < current.value:
            return self._search(current.left, key)

        return self._search(current.right, key)


# 사용 예제
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
bst.inorder_traversal(bst.root)  # 20 30 40 50 60 70 80
print(bst.search(40) is not None)  # True
print(bst.search(90) is not None)  # False
