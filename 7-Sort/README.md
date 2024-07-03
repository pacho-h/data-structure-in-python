# 정렬(Sort)

정렬(Sorting)은 데이터를 특정 순서에 따라 재배열하는 작업이다. 정렬 알고리즘은 다양한 종류가 있으며, 각기 다른 시간 복잡도와 공간 복잡도를 가진다. 여기서는 몇 가지 주요 정렬 알고리즘에 대해 설명하겠다.

## 선택 정렬(Selection Sort)

선택 정렬은 매 단계에서 최소값을 찾아 배열의 앞부분부터 순서대로 배치하는 정렬 알고리즘이다.

**적합한 상황**:

- 데이터가 거의 정렬되어 있는 경우가 아닌 작은 데이터셋.
- 메모리 사용이 중요한 경우 (제자리 정렬).

**예시**:

- 학급의 학생들을 성적 순으로 정렬할 때, 학생 수가 적은 경우.

구현: [selection_sort.py](https://github.com/pacho-h/data-structure-in-python/blob/main/7-Sort/selection_sort.py)

## 삽입 정렬(Insertion Sort)

삽입 정렬은 배열의 요소를 하나씩 순회하면서 정렬된 부분과 비교하여 적절한 위치에 삽입하는 정렬 알고리즘이다.

**적합한 상황**:

- 데이터가 거의 정렬되어 있는 경우.
- 작은 데이터셋.

**예시**:

- 카드 게임에서 플레이어가 손에 들고 있는 카드를 정렬할 때.

구현: [insertion_sort.py](https://github.com/pacho-h/data-structure-in-python/blob/main/7-Sort/insertion_sort.py)

## 버블 정렬(Bubble Sort)

버블 정렬은 인접한 두 요소를 비교하여 필요에 따라 교환하며 배열의 끝까지 이동하는 과정을 반복하는 정렬 알고리즘이다.

**적합한 상황**:

- 간단한 구현이 필요한 작은 데이터셋.
- 학습 목적으로 사용.

**예시**:

- 학생들에게 정렬 알고리즘의 기본 개념을 가르칠 때.

구현: [bubble_sort.py](https://github.com/pacho-h/data-structure-in-python/blob/main/7-Sort/bubble_sort.py)

## 셸 정렬(Shell Sort)

셸 정렬은 삽입 정렬의 일반화된 형태로, 일정한 간격으로 떨어진 요소들을 삽입 정렬하는 과정을 반복하여 정렬하는 알고리즘이다.

**적합한 상황**:

- 중간 크기의 데이터셋.
- 삽입 정렬보다 빠른 성능이 필요한 경우.

**예시**:

- 배열 크기가 중간 정도일 때 효율적으로 정렬을 필요로 하는 경우.

구현: [shell_sort.py](https://github.com/pacho-h/data-structure-in-python/blob/main/7-Sort/shell_sort.py)

## 합병 정렬(Merge Sort)

합병 정렬은 분할 정복 알고리즘으로 배열을 반으로 나누고, 각각을 정렬한 후 합치는 과정으로 이루어진다.

**적합한 상황**:

- 큰 데이터셋.
- 안정 정렬이 필요한 경우.
- 병합이 필요한 경우 (외부 정렬).

**예시**:

- 대규모 데이터베이스의 레코드를 정렬할 때.
- 외부 파일 정렬 시 사용.

구현: [merge_sort.py](https://github.com/pacho-h/data-structure-in-python/blob/main/7-Sort/merge_sort.py)

## 퀵 정렬(Quick Sort)

퀵 정렬은 분할 정복 알고리즘으로, 피벗을 기준으로 배열을 두 부분으로 나눈 후 각각을 정렬하는 과정을 반복한다.

**적합한 상황**:

- 일반적인 경우에 빠른 정렬이 필요한 경우.
- 평균적인 경우에 매우 빠르며, 공간 효율성이 좋은 경우.

**예시**:

- 데이터베이스 쿼리 결과를 정렬할 때.

구현: [quick_sort.py](https://github.com/pacho-h/data-structure-in-python/blob/main/7-Sort/quick_sort.py)

## 히프 정렬(Heap Sort)

히프 정렬은 히프 자료구조를 이용한 정렬 알고리즘으로, 최대 히프 또는 최소 히프를 구성한 후 정렬을 수행한다.

**적합한 상황**:

- 항상 최악의 경우에도 O(n log n) 성능이 보장되어야 하는 경우.
- 추가 메모리를 사용하지 않고 제자리 정렬이 필요한 경우.

**예시**:

- 실시간 시스템에서 일정 시간 내에 정렬이 필요한 경우.

구현: [heap_sort.py](https://github.com/pacho-h/data-structure-in-python/blob/main/7-Sort/heap_sort.py)

## 기수 정렬(Radix Sort)

기수 정렬은 정수 리스트를 자리수별로 정렬하는 알고리즘으로, 각 자리수를 기준으로 정렬을 반복하여 최종 정렬을 완료한다.

**적합한 상황**:

- 키가 비교적 짧고 일정한 경우의 정렬.
- 정수나 문자열 같은 데이터 정렬.

**예시**:

- 도서관의 책을 ISBN 번호로 정렬할 때.
- 긴 문자열을 비교하지 않고 정렬할 때.

구현: [radix_sort.py](https://github.com/pacho-h/data-structure-in-python/blob/main/7-Sort/radix_sort.py)

이와 같이 다양한 정렬 알고리즘은 각기 다른 상황과 조건에서 최적의 성능을 발휘할 수 있다. 필요한 경우에 따라 적절한 정렬 알고리즘을 선택하는 것이 중요하다.
