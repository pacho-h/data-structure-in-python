def floyd_warshall(graph):
    dist = {v: {u: float('infinity') for u in graph} for v in graph}
    for v in graph:
        dist[v][v] = 0
        for u, weight in graph[v]:
            dist[v][u] = weight

    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# 사용 예제
example_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}
print(floyd_warshall(example_graph))
# {'A': {'A': 0, 'B': 1, 'C': 3, 'D': 4}, 'B': {'A': 1, 'B': 0, 'C': 2, 'D': 3}, ...}
