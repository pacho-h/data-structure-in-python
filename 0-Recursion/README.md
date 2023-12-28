# Recursion
(순환, 재귀)
참고: [realpython.com > python-recursion](https://realpython.com/python-recursion)

 프로그래밍에서 재귀(Recursion)라 함은 어떤 함수 내에서 자기 자신을 호출하는 것을 말한다. 이런 함수를 재귀 함수라고 하는데, 거의 대부분의 문제들은 재귀적 방법이 아니더라도 해결이 가능하지만, Tree 처럼 중첩 구조의 순회 알고리즘을 구현하는 경우 재귀적으로 구현 한다면 코드가 더 간결하고 명확해질 수 있다.
  때로 재귀적인 연산으로 인해 지나치게 많은 메모리를 사용하게 되거나 연산 속도가 더 느릴 수 있으니 주의.

code:
```python
// recursion example
// print countdown from n to 0
def countdown(n):
    if n > 0:
        print(n)
        countdown(n-1)
```

result:
```python
>>> countdown(5)
5
4
3
2
1
```

재귀 함수를 호출하는 조건이 없다면 무한히 호출될 수 있는데, Python 의 재귀 중첩 수의 제한은 sys module 의 getrecursionlimit() 함수를 호출하여 확인하고 setrecursionlimit() 함수로 설정할 수 있다.(기본값은 1000)

```python
>>> from sys import getrecursionlimit, setrecursionlimit
>>> getrecursionlimit()
1000
>>> setrecursionlimit(2000)
>>> getrecursionlimit()
2000
```


## factorial
자연수의 계승, `!` 기호를 사용한다.

```
n! = 1 * 2 * 3 * ... * n
```

factorial 은 다음과 같이 정의할 수 있다.
```
n! : n == 0 OR n == 1 -> return 1
     n > 1 -> return n * (n-1)!
```

구현: factorial.py

## exponentiation
거듭제곱
정수부(base)와 지수부(exponent)로 구분된다.
```
2^8 = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 = 256
2의 8승이라고도 하며, 2를 8번 곱한다.
```

구현: exponentiation.py
