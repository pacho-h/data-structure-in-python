# Array
(배열)
참고: [realpython.com > python-array](https://realpython.com/python-array)

  python의 array는 숫자 데이터(numeric data)를 효율적으로 사용하기 위한 자료구조라고 소개한다. 설명한 것처럼 python의 array에는 숫자 자료형만 저장할 수 있다.
  프로그래밍에서 배열(array)이란 동일한 타입의 변수가 메모리상에 연속적으로 이어진 구조를 말하고 다음과 같은 특징을 가진다.
 - 배열을 구성하는 원소들은 동일한 자료형(type)으로 이루어진다.
 - 배열을 구성하는 원소들은 메모리상에 연속적으로 이어진 공간을 가진다.
 - 배열은 메모리상에 고정된 크기의 공간을 가진다.(이어진 공간을 할당하기 때문에 한 번 할당 한뒤에 확장할 수 없다.)

  처음 두가지 특징 덕분에 배열 인덱스와 자료형의 크기만 알고 있으면 특정 인덱스의 주소값을 계산할 수 있다.

  > Array[index] 의 주소값 == Array[0] 의 주소값 + 자료형의 크기(byte) * index

  덕분에 이후에 특정 인덱스의 값을 참조하기 위해 0번째 주소부터 순회할 필요 없이 위의 공식으로 해당 주소를 직접 참조할 수 있다. 원소를 삽입/삭제 하거나 배열의 크기를 변경할 수 없기 때문에 배열의 원소를 삽입/삭제하거나 배열을 확장할 때는 새로운 배열을 만들고(메모리 공간을 할당하고) 값을 복사하는 방법을 이용한다. 이는 더 큰 메모리 공간을 새로 할당하고 값들을 복사하는 등의 작업이 반복되기 때문에 비효율 적이다.

  이 제한을 완화하기 위해 필요한 크기보다 더 큰 메모리공간을 할당하고 메모리 공간대비 현재 저장된 원소의 수를 추적하여 일정 수준 이상의 원소를 저장했을때 메모리 공간을 더 할당해서 메모리 할당, 값 복사 작업의 빈도를 줄일 수 있다.

  이후에 나오는 리스트(List)와 비교하면, 배열은 원소의 삽입/삭제 빈도가 높은 작업에는 비효율적이며 조회 빈도가 높은 작업에 적합하다. 리스트는 반대로 조회 작업보다는 삽입/삭제가 많은 작업에 더 적합하다.

## Python array

```python
array(typecode[, initializer])
```

typecode reference:

```bash
┌─────────────┬────────────────────┬───────────────────┬─────────────────────────┐
│ Type code   │ C Type             │ Python Type       │   Minimum size in bytes │
├─────────────┼────────────────────┼───────────────────┼─────────────────────────┤
│ 'b'         │ signed char        │ int               │                       1 │
│ 'B'         │ unsigned char      │ int               │                       1 │
│ 'u'         │ wchar_t            │ Unicode character │                       2 │
│ 'h'         │ signed short       │ int               │                       2 │
│ 'H'         │ unsigned short     │ int               │                       2 │
│ 'i'         │ signed int         │ int               │                       2 │
│ 'I'         │ unsigned int       │ int               │                       2 │
│ 'l'         │ signed long        │ int               │                       4 │
│ 'L'         │ unsigned long      │ int               │                       4 │
│ 'q'         │ signed long long   │ int               │                       8 │
│ 'Q'         │ unsigned long long │ int               │                       8 │
│ 'f'         │ float              │ float             │                       4 │
│ 'd'         │ double             │ float             │                       8 │
└─────────────┴────────────────────┴───────────────────┴─────────────────────────┘
```

사용 예시
```python
>>> array("i", [2 ** i for i in range(8)])
array('i', [1, 2, 4, 8, 16, 32, 64, 128])

>>> array("d", (1.4, 2.8, 4, 5.6))
array('d', [1.4, 2.8, 4.0, 5.6])

>>> array("u", "café")
array('u', 'café')

>>> array("u", ["c", "a", "f", "é"])
array('u', 'café')
```

## Python list

  Python에는 list 라는 자료형이 있는데 C의 array와 같지만 다르다. CPython을 보면 실제로 C array를 활용해서 Python list를 구현했다. list 객체를 정의할 때 크기(길이)를 지정하지 않아도 되는데, list는 동적배열으로서 원소를 저장할 때 할당 받은 메모리 공간을 모두 사용하면 더 큰 크기의 배열을 새로 선언(resize)하여 사용하기 때문이다.

# 배열의 응용: 다항식

<img src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Terms-coefficient-ko.svg" style="background-color: white; width: 400px;" title="polynomial"/>

출처: [위키백과-다항식](https://ko.wikipedia.org/wiki/%EB%8B%A4%ED%95%AD%EC%8B%9D)

다항식이란, 한 개 또는 두 개 이상의 항의 합으로 이루어진 식으로 계수, 변수, 차수로 구성된 변수항과 상수항으로 이루어져있다.

다항식의 각 항을 배열의 원소로 표현할 수 있다. 다항식에서 가장 높은 차수만큼의 크기의 배열에 n~0차항의 계수를 저장한다. 이 배열을 활용하여 다항식끼리의 덧셈과 곱샘을 계산을 구현할 수 있다.

아래의 배열은 4차 다항식을 표현한 것이다.
```
polynomial1
┌───┬───┬───┬───┬───┐
│ 2 │ 0 │ 4 │ 1 │ 3 │
└───┴───┴───┴───┴───┘
= 2*x^4 + 0*x^3 + 4*x^2 + 1*x^1 + 3(*x^0) 

polynomial2
┌───┬───┐
│ 5 │ 6 │
└───┴───┘
= 5*x^1 + 6*x^0
```

Python 코드로 작성하면
```python
# index를 차수로 사용하기 위해 다항식 차수의 오름차순으로 생성
polynomial1 = [3, 1, 4, 0, 2]
polynomial2 = [6, 5]
```

- 다항식의 덧셈: 동차항끼리의 계수를 합한다.
- 다항식의 곱셈: 분배법칙 이용, 두 항의 곱셈은 계수끼리 곱하고, 동일한 변수의 차수끼리 더한다.

구현: [polynomial.py](https://github.com/pacho-h/data-structure-in-python/blob/main/1-Array/polynomial.py)

# 배열의 응용: 희소 행렬(Sparse Matrix)

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/dbbd270e3e174daa36d9c2460211fe6f8569c0e6" style="background-color: white; width: 400px;" title="sparse matrix"/>

출처: [위키백과-성긴 행렬](https://ko.wikipedia.org/wiki/%EC%84%B1%EA%B8%B4_%ED%96%89%EB%A0%AC)

희소 행렬(성긴 행렬; sparse matrix)이란, 대부분의 값이 0인 행렬을 말한다.
2차원 배열을 활용하여 간단히 행렬을 구현할 수 있는데 희소 행렬처럼 같은 값(0)이 대부분이고 특정 좌표에만 다른 값이 저장 되어 있는 경우, 다른(0이 아닌)값이 저장된 곳의 위치(행,열)와 값만을 저장하여 메모리 공간을 절약할 수 있다.

2차원으로 표현한 희소 행렬:

```python
# 희소 행렬
matrix = [[0, 0, 0, 0, 0],
          [0, 5, 0, 0, 0],
          [0, 0, 0, 3, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 7]]

# 0이 아닌 값만 위치와 값을 Tuple List로 표현
# [(행, 열, 값), ...]
sparse_matrix = [(1, 1, 5),
                 (2, 3, 3),
                 (4, 5, 7)]
```

구현: [sparse-matrix.py](https://github.com/pacho-h/data-structure-in-python/blob/main/1-Array/sparse-matrix.py)

