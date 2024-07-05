# 트리(Tree)

트리(Tree)는 계층적인 구조를 가진 자료구조로, 루트(root) 노드에서 시작하여 자식 노드(child nodes)로 분기하는 방식으로 구성된다. 트리는 노드와 에지(edge)로 구성되며, 각 노드는 부모(parent) 노드와 자식 노드로 연결된다.

## 이진 트리

이진 트리(Binary Tree)는 각 노드가 최대 두 개의 자식 노드를 가지는 트리이다. 자식 노드는 왼쪽 자식(left child)과 오른쪽 자식(right child)으로 구분된다.

구현: [binary_tree.py](https://github.com/pacho-h/data-structure-in-python/blob/main/5-Tree/binary_tree.py)

## 스레드 이진 트리

스레드 이진 트리(Threaded Binary Tree)는 각 노드의 왼쪽 및 오른쪽 포인터를 사용하여 중위 순회의 다음 노드를 가리키도록 하는 트리이다. 이는 트리 순회를 더 효율적으로 수행할 수 있게 해준다.

구현: [threaded_binary_tree.py](https://github.com/pacho-h/data-structure-in-python/blob/main/5-Tree/treaded_binary_tree.py)

## 이진 탐색 트리

이진 탐색 트리(Binary Search Tree, BST)는 각 노드가 키(key)를 가지며, 왼쪽 자식 노드의 키는 현재 노드의 키보다 작고, 오른쪽 자식 노드의 키는 현재 노드의 키보다 큰 구조를 가진다.

구현: [binary_search_tree.py](https://github.com/pacho-h/data-structure-in-python/blob/main/5-Tree/binary_search_tree.py)

## 이진 탐색 트리의 응용: 영어 사전

이진 탐색 트리는 영어 사전과 같은 응용 프로그램에서 단어를 저장하고 검색하는 데 유용하다. 각 단어를 이진 탐색 트리의 노드로 저장할 수 있다.

구현: [en_dict.py](https://github.com/pacho-h/data-structure-in-python/blob/main/5-Tree/en_dict.py)

이와 같이 트리는 다양한 자료를 효율적으로 저장하고 검색하는 데 사용될 수 있다. 이진 트리, 스레드 이진 트리, 이진 탐색 트리 등의 구조를 통해 다양한 응용 프로그램에서 활용할 수 있다.
