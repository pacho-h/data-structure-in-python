class Node2_3_4:
    def __init__(self, keys=[]):
        self.keys = keys
        self.children = []


class Tree2_3_4:
    def __init__(self):
        self.root = None

    def search(self, node, key):
        if not node:
            return None
        if key in node.keys:
            return node
        if not node.children:
            return None
        if key < node.keys[0]:
            return self.search(node.children[0], key)
        if len(node.keys) == 1 or (len(node.keys) == 2 and key < node.keys[1]):
            return self.search(node.children[1], key)
        if len(node.keys) == 2 or (len(node.keys) == 3 and key < node.keys[2]):
            return self.search(node.children[2], key)
        return self.search(node.children[3], key)

    def insert(self, key):
        if not self.root:
            self.root = Node2_3_4([key])
            return
        self.root = self._insert(self.root, key)
        if len(self.root.keys) == 4:
            self.root = self._split(self.root)

    def _insert(self, node, key):
        if not node.children:
            node.keys.append(key)
            node.keys.sort()
        else:
            if key < node.keys[0]:
                child = self._insert(node.children[0], key)
            elif len(node.keys) == 1 or (len(node.keys) == 2 and key < node.keys[1]):
                child = self._insert(node.children[1], key)
            elif len(node.keys) == 2 or (len(node.keys) == 3 and key < node.keys[2]):
                child = self._insert(node.children[2], key)
            else:
                child = self._insert(node.children[3], key)

            if len(child.keys) == 4:
                new_child, median = self._split(child)
                index = node.children.index(child)
                node.children[index] = new_child
                node.keys.append(median)
                node.keys.sort()
                node.children.insert(index + 1, new_child)

        return node

    def _split(self, node):
        left = Node2_3_4([node.keys[0]])
        right = Node2_3_4([node.keys[2]])
        median = node.keys[1]
        if node.children:
            left.children = node.children[:2]
            right.children = node.children[2:]
        return left, median, right


# 사용 예제
tree_2_3_4 = Tree2_3_4()
keys_2_3_4 = [10, 20, 5, 6, 12, 30, 7, 17]
for key in keys_2_3_4:
    tree_2_3_4.insert(key)
print(tree_2_3_4.root.keys)  # [10, 20]
print([child.keys for child in tree_2_3_4.root.children])  # [[5, 6, 7], [12, 17], [30]]
