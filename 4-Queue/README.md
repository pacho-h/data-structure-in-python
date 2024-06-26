# 큐(Queue)

큐(Queue)는 데이터를 순서대로 저장하고, 먼저 저장된 데이터를 먼저 꺼내는 선입선출(FIFO, First In First Out) 방식의 자료구조다.
큐는 일상생활에서 접할 수 있는 여러 예시, 예를 들어 줄 서기, 프린터 작업 대기열 등에 비유할 수 있다.

## 큐 추상 데이터 타입

큐 추상 데이터 타입(ADT, Abstract Data Type)은 큐가 수행해야 하는 기본적인 연산들을 정의한다. 주요 연산은 다음과 같다:

- `enqueue(item)`: 큐의 맨 뒤에 아이템을 추가한다.
- `dequeue()`: 큐의 맨 앞에 있는 아이템을 제거하고 반환한다.
- `front()`: 큐의 맨 앞에 있는 아이템을 제거하지 않고 반환한다.
- `is_empty()`: 큐가 비어 있는지 여부를 확인한다.
- `size()`: 큐에 있는 아이템의 수를 반환한다.

## 배열로 구현된 큐

배열로 큐를 구현하는 방식은 간단하고 직관적이다. 파이썬에서는 리스트를 이용해 쉽게 큐를 구현할 수 있다.

구현: [array_queue.py](https://github.com/pacho-h/data-structure-in-python/blob/main/4-Queue/array_queue.py)

## 연결 리스트로 구현된 큐

연결 리스트로 큐를 구현하면, 동적 메모리 할당을 통해 유연하게 크기를 조절할 수 있다.

구현: [linked_list_queue.py](https://github.com/pacho-h/data-structure-in-python/blob/main/4-Queue/linked_list_queue.py)

## 덱(Deque)

덱(Deque, Double-Ended Queue)은 양쪽 끝에서 삽입과 삭제가 모두 가능한 큐다. 파이썬에서는 `collections` 모듈의 `deque` 클래스를 이용해 덱을 쉽게 구현할 수 있다.

구현: [double_ended_queue.py](https://github.com/pacho-h/data-structure-in-python/blob/main/4-Queue/double_ended_queue.py)

## 큐의 응용

큐는 다양한 응용 분야에서 사용된다. 그 중 몇 가지 예를 들어보겠다.

### 너비 우선 탐색(BFS)

큐는 그래프 탐색에서 너비 우선 탐색(BFS, Breadth-First Search)을 구현하는 데 사용된다.

구현: [breadth_first_search.py](https://github.com/pacho-h/data-structure-in-python/blob/main/4-Queue/breadth_first_search.py)

### 캐시 구현

큐는 캐시 시스템을 구현할 때도 사용된다. 예를 들어, 최근에 사용된 페이지를 추적하기 위해 FIFO 방식의 큐를 사용할 수 있다.

구현: [page_cache.py](https://github.com/pacho-h/data-structure-in-python/blob/main/4-Queue/page_cache.py)

이와 같이 큐는 다양한 문제에 활용될 수 있으며, 배열이나 연결 리스트로 구현하는 방식에 따라 그 특성이 달라지므로, 상황에 맞게 적절한 구현 방식을 선택하는 것이 중요하다.