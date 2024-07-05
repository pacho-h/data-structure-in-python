# 해싱(Hashing)

해싱(Hashing)은 키를 사용하여 데이터를 빠르게 검색하고 저장하는 기술이다. 해싱을 사용하면 데이터 검색, 삽입, 삭제의 시간 복잡도를 평균적으로 O(1)로 만들 수 있다. 여기에서는 해싱의 개념과 관련된 다양한 주제를 다룬다.

## 추상 자료형 사전 구조

추상 자료형(ADT, Abstract Data Type) 사전(Dictionary)은 키(key)와 값(value) 쌍의 집합으로, 각 키는 고유하며 값을 통해 데이터를 접근할 수 있다. 사전은 다음과 같은 연산을 제공한다:

- `insert(key, value)`: 키와 값을 삽입한다.
- `delete(key)`: 키에 해당하는 값을 삭제한다.
- `search(key)`: 키에 해당하는 값을 검색한다.

파이썬에서는 사전을 `dict` 타입으로 쉽게 사용할 수 있다.

```python
# 사전의 기본 사용 예제
my_dict = {}
my_dict['name'] = 'Alice'
my_dict['age'] = 25

print(my_dict['name'])  # Alice
print(my_dict.get('age'))  # 25
my_dict.pop('name')
print(my_dict)  # {'age': 25}
```

## 해싱의 구조

해싱의 기본 구조는 해시 테이블(Hash Table)로, 키를 해시 함수(Hash Function)에 입력하여 나온 해시 값을 인덱스로 사용해 값을 저장하는 방식이다. 해시 테이블의 주요 구성 요소는 다음과 같다:

- 해시 함수(Hash Function): 키를 입력으로 받아 해시 값을 반환한다.
- 버킷(Bucket): 해시 테이블의 각 슬롯으로, 실제 데이터를 저장하는 곳이다.

## 해시 함수

해시 함수는 키를 해시 테이블의 인덱스로 변환하는 함수다. 해시 함수는 다음과 같은 특성을 가져야 한다:

- 효율적이어야 한다.
- 가능한 균등하게 해시 값을 분포시켜야 한다.

파이썬의 기본 해시 함수는 `hash()` 함수를 사용하여 구현할 수 있다.

```python
# 해시 함수 사용 예제
print(hash('Alice'))  # 키 'Alice'의 해시 값
print(hash('Bob'))  # 키 'Bob'의 해시 값
```

## 충돌 해결책

해시 함수가 서로 다른 키에 대해 동일한 해시 값을 반환하는 경우 충돌(Collision)이 발생한다. 충돌을 해결하는 방법에는 여러 가지가 있다.

### 선형 조사법(Linear Probing)

선형 조사법은 충돌이 발생하면 해시 테이블에서 다음 빈 슬롯을 찾는 방법이다.

구현: [linear_probing.py](https://github.com/pacho-h/data-structure-in-python/blob/main/9-Hashing/linear_probing.py)

### 체이닝(Chaining)

체이닝은 각 버킷을 연결 리스트로 구성하여 충돌을 해결하는 방법이다.

구현: [chaining.py](https://github.com/pacho-h/data-structure-in-python/blob/main/9-Hashing/chaining.py)

## 해싱의 성능 분석

해싱의 성능은 주로 다음과 같은 요소에 의해 결정된다:

- 해시 함수의 효율성: 해시 함수가 키를 고르게 분포시킬수록 충돌이 줄어든다.
- 해시 테이블의 크기: 해시 테이블의 크기가 충분히 크다면 충돌이 줄어든다.
- 충돌 해결 방법: 충돌을 효율적으로 해결할 수 있는 방법을 선택하는 것이 중요하다.

### 평균적인 시간 복잡도

- `insert`: O(1)
- `search`: O(1)
- `delete`: O(1)

### 최악의 시간 복잡도

충돌이 많이 발생하는 경우 최악의 시간 복잡도는 O(n)까지 증가할 수 있다. 따라서 해시 테이블의 크기와 해시 함수의 선택이 매우 중요하다.

해싱은 데이터 검색, 삽입, 삭제의 평균 시간 복잡도가 O(1)로 매우 효율적이므로 다양한 응용 프로그램에서 널리 사용된다. 적절한 해시 함수와 충돌 해결 방법을 선택하는 것이 해싱 성능의 핵심이다.
