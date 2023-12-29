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


## Fibonacci numbers
피보나치 수
0번째 항이 0, 1번째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열이다.
```
피보나치 수 F
F[0] = 0
F[1] = 1
F[n] = F[n - 2] + F[n - 1]  # (if n > 2)
```

구현: fibonacci_numbers.py


## Tower of Hanoi
하노이의 탑
> 하노이의 탑은 프랑스의 수학자인 에두아르 뤼카(Édouard Lucas)가 클라우스 교수(professeur N. Claus)라는 필명으로 1883년에 발표하였다.[2] 1년 후 드 파르빌(Henri de Parville)은 Claus가 Lucas의 애너그램임을 밝히면서 다음과 같은 이야기로 하노이의 탑을 소개하였다.
"인도 베나레스에 있는 한 사원에는 세상의 중심을 나타내는 큰 돔이 있고 그 안에 세 개의 다이아몬드 바늘이 동판 위에 세워져 있습니다. 바늘의 높이는 1 큐빗이고 굵기는 벌의 몸통만 합니다. 바늘 가운데 하나에는 신이 64개의 순금 원판을 끼워 놓았습니다. 가장 큰 원판이 바닥에 놓여 있고, 나머지 원판들이 점점 작아지며 꼭대기까지 쌓아 있습니다. 이것은 신성한 브라흐마의 탑입니다. 브라흐마의 지시에 따라 승려들은 모든 원판을 다른 바늘로 옮기기 위해 밤낮 없이 차례로 제단에 올라 규칙에 따라 원판을 하나씩 옮깁니다. 이 일이 끝날 때, 탑은 무너지고 세상은 종말을 맞이하게 됩니다."
이후 라우즈 볼, 가드너 등이 하노이의 탑을 소개하면서 널리 알려졌다.
출처: https://ko.wikipedia.org/wiki/%ED%95%98%EB%85%B8%EC%9D%B4%EC%9D%98_%ED%83%91

게임의 목적은 다음 두 가지 조건을 만족시키면서, 한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서 다시 쌓는 것이다.
- 한 번에 한개의 원판만 옮길 수 있다.
- 가장 위에 있는 원판만 이동할 수 있다.
- 큰 원판이 작은 원판 위에 있어서는 안 된다.

일반적으로 원판이 n개 일 때, 2^n -1번의 이동으로 원판을 모두 옮길 수 있다

