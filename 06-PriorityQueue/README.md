# 우선순위 큐(Priority Queue)

우선순위 큐(Priority Queue)는 각 요소가 우선순위를 가지고 있는 자료구조다. 일반 큐와는 달리, 우선순위 큐에서는 우선순위가 높은 요소가 먼저 처리된다.

## 우선순위 큐 추상 데이터 타입

우선순위 큐 추상 데이터 타입(ADT, Abstract Data Type)은 다음과 같은 연산들을 정의한다:

- `insert(item, priority)`: 우선순위 큐에 우선순위와 함께 아이템을 추가한다.
- `extract_max()`: 우선순위 큐에서 우선순위가 가장 높은 아이템을 제거하고 반환한다.
- `peek()`: 우선순위 큐에서 우선순위가 가장 높은 아이템을 제거하지 않고 반환한다.
- `is_empty()`: 우선순위 큐가 비어 있는지 여부를 확인한다.
- `size()`: 우선순위 큐에 있는 아이템의 수를 반환한다.

## 우선순위 큐의 구현 방법

우선순위 큐는 배열, 연결 리스트, 히프(Heap) 등을 이용하여 구현할 수 있다. 가장 효율적인 방법은 히프를 사용하는 것이다.

### 배열로 구현된 우선순위 큐

구현: [array_priority_queue.py](https://github.com/pacho-h/data-structure-in-python/blob/main/6-PriorityQueue/array_priority_queue.py)

### 연결 리스트로 구현된 우선순위 큐

구현: [linked_list_priority_queue.py](https://github.com/pacho-h/data-structure-in-python/blob/main/6-PriorityQueue/linked_list_priority_queue.py)

## 히프(Heap)

히프는 완전 이진 트리의 일종으로, 항상 최대값(또는 최소값)을 루트에 위치시키는 자료구조다. 히프는 두 가지 종류가 있다:

- 최대 히프(Max Heap): 부모 노드의 값이 자식 노드의 값보다 크거나 같다.
- 최소 히프(Min Heap): 부모 노드의 값이 자식 노드의 값보다 작거나 같다.

### 히프로 구현된 우선순위 큐

파이썬에서는 `heapq` 모듈을 사용하여 히프를 쉽게 구현할 수 있다. 기본적으로 `heapq`는 최소 히프를 제공하므로, 최대 히프를 구현하려면 우선순위의 부호를 반대로 사용해야 한다.

구현: [heap_priority_queue.py](https://github.com/pacho-h/data-structure-in-python/blob/main/6-PriorityQueue/heap_priority_queue.py)

## 히프의 복잡도 분석

- `insert`: O(log n)
- `extract_max`: O(log n)
- `peek`: O(1)

히프는 균형 잡힌 완전 이진 트리이므로, 삽입과 삭제 연산 모두 트리의 높이에 비례하는 시간 복잡도를 가진다. 트리의 높이는 log n에 비례하므로, 히프의 삽입과 삭제 연산의 시간 복잡도는 O(log n)이다.
루트 노드의 값만 확인하는 `peek` 연산은 O(1)의 시간 복잡도를 가진다.

## 히프의 응용

히프는 다양한 응용 분야에서 사용된다. 대표적인 예로 다음과 같은 것이 있다:

1. **우선순위 큐**: 히프는 우선순위 큐의 효율적인 구현을 제공한다.
2. **힙 정렬(Heap Sort)**: 힙 정렬은 O(n log n) 시간 복잡도를 가지며, 안정적이지 않지만 제자리 정렬(in-place sort)이다.
3. **다익스트라 알고리즘**: 힙을 사용하여 그래프에서 최단 경로를 찾는 다익스트라 알고리즘의 효율성을 높일 수 있다.
4. **이벤트 시뮬레이션**: 힙을 사용하여 시뮬레이션 이벤트를 효율적으로 관리할 수 있다.

구현: [heap_sort.py](https://github.com/pacho-h/data-structure-in-python/blob/main/6-PriorityQueue/heap_sort.py)

이와 같이 히프는 우선순위 큐, 정렬 알고리즘, 그래프 알고리즘 등 다양한 분야에서 유용하게 사용된다.