class ThreadedNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.lthread = True
        self.rthread = True


class ThreadedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = ThreadedNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.value:
            if current.lthread:
                new_node = ThreadedNode(key)
                new_node.left = current.left
                new_node.right = current
                current.left = new_node
                current.lthread = False
            else:
                self._insert(current.left, key)
        else:
            if current.rthread:
                new_node = ThreadedNode(key)
                new_node.right = current.right
                new_node.left = current
                current.right = new_node
                current.rthread = False
            else:
                self._insert(current.right, key)

    def inorder_traversal(self):
        current = self.root
        while not current.lthread:
            current = current.left

        while current:
            print(current.value, end=' ')
            if current.rthread:
                current = current.right
            else:
                current = current.right
                while current and not current.lthread:
                    current = current.left


# 사용 예제
tree = ThreadedBinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)
tree.inorder_traversal()  # 20 30 40 50 60 70 80
