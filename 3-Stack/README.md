# 스택(Stack)

스택(Stack)은 자료를 순서대로 저장하고, 나중에 저장한 자료를 가장 먼저 꺼내는 후입선출(LIFO, Last In First Out) 방식의 자료구조다.
스택은 일상생활에서 접할 수 있는 여러 예시, 예를 들어 접시 쌓기, 되돌리기 기능(undo) 등에 비유할 수 있다. 

## 스택 추상 데이터 타입

스택 추상 데이터 타입(ADT, Abstract Data Type)은 스택이 수행해야 하는 기본적인 연산들을 정의한다.
주요 연산은 다음과 같다:

- `push(item)`: 스택의 맨 위에 아이템을 추가.
- `pop()`: 스택의 맨 위에 있는 아이템을 제거하고 반환.
- `peek()`: 스택의 맨 위에 있는 아이템을 제거하지 않고 반환.
- `is_empty()`: 스택이 비어 있는지 여부를 확인.
- `size()`: 스택에 있는 아이템의 수를 반환.

## 배열로 구현한 스택

배열로 스택을 구현하는 방식은 간단하고 직관적이며,
파이썬에서는 리스트를 이용해 쉽게 스택을 구현할 수 있다.

구현: [array_stack.py](https://github.com/pacho-h/data-structure-in-python/blob/main/3-Stack/array_stack.py)

## 연결 리스트로 구현한 스택

연결 리스트로 스택을 구현하면, 동적 메모리 할당을 통해 유연하게 크기를 조절할 수 있다.

구현: [linked_list_stack.py](https://github.com/pacho-h/data-structure-in-python/blob/main/3-Stack/linked_list_stack.py)

## 괄호 검사

스택을 이용하여 괄호의 짝이 맞는지 검사하는 문제는 전형적인 스택 응용 문제.

구현: [bracket_balance.py](https://github.com/pacho-h/data-structure-in-python/blob/main/3-Stack/bracket_balance.py)

## 수식의 계산

스택을 이용하여 후위 표기법(Reverse Polish Notation, RPN)으로 표현된 수식을 계산하는 예제.

구현: [reverse_polish_notation.py](https://github.com/pacho-h/data-structure-in-python/blob/main/3-Stack/reverse_polish_notation.py)

## 미로 탐색 문제

스택을 이용하여 미로를 탐색하는 깊이 우선 탐색(DFS) 알고리즘 구현.

구현: [maze.py](https://github.com/pacho-h/data-structure-in-python/blob/main/3-Stack/maze.py)

이와 같이 스택을 다양한 문제에 활용할 수 있다. 배열이나 연결 리스트로 스택을 구현하는 방식에 따라 그 특성이 달라지므로, 상황에 맞게 적절한 구현 방식을 선택하는 것이 중요하다.