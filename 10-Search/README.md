# 탐색(Search)

탐색은 데이터 구조에서 특정 요소를 찾는 과정이다. 탐색 알고리즘은 다양한 데이터 구조에 따라 최적화되어 있으며, 각기 다른 시간 복잡도를 가진다. 여기에서는 여러 탐색 방법을 설명하겠다.

## 정렬되지 않은 배열에서의 탐색

정렬되지 않은 배열에서의 탐색은 순차 탐색(Sequential Search)을 사용한다. 배열의 처음부터 끝까지 요소를 하나씩 비교하여 목표 값을 찾는다.

구현: [sequential_search.py](https://github.com/pacho-h/data-structure-in-python/blob/main/10-Search/sequential_search.py)

## 정렬된 배열에서의 탐색

정렬된 배열에서의 탐색은 일반적으로 이진 탐색(Binary Search)을 사용한다. 이진 탐색은 배열의 중앙 요소와 목표 값을 비교하여 범위를 절반으로 줄이며 탐색을 진행한다.

## 정렬된 배열에서의 순차 탐색

정렬된 배열에서의 순차 탐색은 순차 탐색과 동일하지만, 목표 값보다 큰 요소를 만나면 탐색을 중단할 수 있다.

구현: [sequential_search_sorted.py](https://github.com/pacho-h/data-structure-in-python/blob/main/10-Search/sequential_search_sorted.py)

## 이진 탐색(Binary Search)

이진 탐색은 정렬된 배열에서 매우 효율적인 탐색 방법이다. 배열의 중간 요소를 기준으로 반씩 나누어 탐색을 진행한다.

구현: [binary_search.py](https://github.com/pacho-h/data-structure-in-python/blob/main/10-Search/binary_search.py)

## 색인 순차 탐색(Indexed Sequential Search)

색인 순차 탐색은 큰 데이터셋을 작은 블록으로 나누고, 각 블록의 시작 요소를 색인으로 저장하여 탐색을 가속화하는 방법이다.

구현: [indexed_sequential_search.py](https://github.com/pacho-h/data-structure-in-python/blob/main/10-Search/indexed_sequential_search.py)

## 보간 탐색(Interpolation Search)

보간 탐색은 이진 탐색과 비슷하지만, 목표 값이 있을 것으로 예상되는 위치를 계산하여 탐색을 진행한다.

구현: [interpolation_search.py](https://github.com/pacho-h/data-structure-in-python/blob/main/10-Search/interpolation_search.py)

## 균형 이진 탐색 트리

균형 이진 탐색 트리는 삽입, 삭제 후에도 트리의 균형을 유지하는 이진 탐색 트리다. 이는 최악의 경우에도 O(log n) 시간 복잡도를 보장한다.

### AVL 트리

AVL 트리는 각 노드의 두 자식 서브트리 높이 차이가 최대 1이 되도록 유지하는 균형 이진 탐색 트리이다.

구현: [avl.py](https://github.com/pacho-h/data-structure-in-python/blob/main/10-Search/avl.py)

## 2-3 트리

2-3 트리는 각 노드가 2개 또는 3개의 자식을 가지는 균형 트리다. 모든 리프 노드는 같은 깊이에 있으며, 삽입과 삭제 연산이 균형을 유지하도록 한다.

구현: [2_3.py](https://github.com/pacho-h/data-structure-in-python/blob/main/10-Search/2_3.py)

## 2-3-4 트리

2-3-4 트리는 2-3 트리의 일반화된 형태로, 각 노드가 최대 4개의 자식과 3개의 키를 가질 수 있는 균형 트리다. 모든 리프 노드는 같은 깊이에 있으며, 삽입과 삭제 연산이 균형을 유지하도록 한다.

구현: [2_3_4.py](https://github.com/pacho-h/data-structure-in-python/blob/main/10-Search/2_3_4.py)

이와 같이 다양한 탐색 알고리즘과 트리 구조를 통해 데이터 구조에서 효율적으로 요소를 찾고 관리할 수 있다. 각 알고리즘과 구조는 특정 상황에서 더 적합할 수 있으며, 그에 따라 선택하여 사용해야 한다.