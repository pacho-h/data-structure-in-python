# 그래프(Graph)

그래프(Graph)는 정점(Vertex)와 간선(Edge)으로 구성된 자료구조로, 다양한 네트워크와 관계를 모델링할 수 있다. 그래프는 방향성, 가중치 등에 따라 여러 가지 유형으로 나눌 수 있다.

## 그래프 추상 데이터 타입

그래프 추상 데이터 타입(ADT, Abstract Data Type)은 다음과 같은 연산들을 정의한다:

- `add_vertex(v)`: 그래프에 정점 `v`를 추가한다.
- `add_edge(v, w)`: 정점 `v`와 정점 `w`를 연결하는 간선을 추가한다.
- `get_vertices()`: 그래프에 있는 모든 정점을 반환한다.
- `get_edges()`: 그래프에 있는 모든 간선을 반환한다.

### 그래프의 구현

파이썬에서는 딕셔너리로 그래프를 구현할 수 있다. 정점은 키로, 간선은 값으로 저장한다.

구현: [graph.py](https://github.com/pacho-h/data-structure-in-python/blob/main/8-Graph/graph.py)

## 그래프의 탐색

### 깊이 우선 탐색(DFS, Depth-First Search)

깊이 우선 탐색은 그래프의 정점을 깊게 탐색하는 방법이다. 스택을 사용하거나 재귀를 통해 구현할 수 있다.

구현: [dfs.py](https://github.com/pacho-h/data-structure-in-python/blob/main/8-Graph/dfs.py)

### 너비 우선 탐색(BFS, Breadth-First Search)

너비 우선 탐색은 그래프의 정점을 넓게 탐색하는 방법이다. 큐를 사용하여 구현할 수 있다.

구현: [bfs.py](https://github.com/pacho-h/data-structure-in-python/blob/main/8-Graph/bfs.py)

## 연결 성분

연결 성분은 무향 그래프에서 서로 연결된 정점들의 최대 부분 집합을 의미한다.

구현: [connected_components.py](https://github.com/pacho-h/data-structure-in-python/blob/main/8-Graph/connected_components.py)

## 신장 트리

신장 트리는 그래프의 모든 정점을 포함하며 사이클이 없는 최소 연결 부분 그래프다.

### 최소 비용 신장 트리(MST, Minimum Spanning Tree)

최소 비용 신장 트리는 그래프의 모든 정점을 연결하는 데 필요한 최소 비용의 간선 집합이다.

#### Kruskal의 MST 알고리즘

Kruskal 알고리즘은 간선을 가중치 순으로 정렬하여 최소 비용 신장 트리를 구성한다.

구현: [kruskal.py](https://github.com/pacho-h/data-structure-in-python/blob/main/8-Graph/kruskal.py)

#### Prim의 MST 알고리즘

Prim 알고리즘은 하나의 정점에서 시작하여 연결된 가장 작은 가중치의 간선을 선택하며 MST를 확장한다.

구현: [prim.py](https://github.com/pacho-h/data-structure-in-python/blob/main/8-Graph/prim.py)

## 최단 경로

### Dijkstra의 최단 경로 알고리즘

Dijkstra 알고리즘은 가중치 그래프에서 한 정점에서 다른 모든 정점으로의 최단 경로를 찾는다.

구현: [dijkstra.py](https://github.com/pacho-h/data-structure-in-python/blob/main/8-Graph/dijkstra.py)

### Floyd의 최단 경로 알고리즘

Floyd-Warshall 알고리즘은 모든 정점 쌍 간의  최단 경로를 찾는 알고리즘이다.

구현: [floyd.py](https://github.com/pacho-h/data-structure-in-python/blob/main/8-Graph/floyd.py)

## 위상 정렬

위상 정렬은 방향 그래프에서 각 정점을 선형 순서로 나열하는 것이다. 주로 작업 순서를 찾는 데 사용된다.

구현: [topological_sort.py](https://github.com/pacho-h/data-structure-in-python/blob/main/8-Graph/topological_sort.py)

이와 같이 그래프의 다양한 개념과 알고리즘을 통해 네트워크와 관계를 모델링하고, 최단 경로, 최소 비용 신장 트리, 위상 정렬 등을 효율적으로 처리할 수 있다.
