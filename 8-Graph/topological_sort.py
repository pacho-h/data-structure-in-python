from collections import deque


def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in graph if in_degree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) == len(in_degree):
        return topo_order
    else:
        return 'Cycle exists'


# 사용 예제
example_graph = {'A': ['C'], 'B': ['C', 'D'], 'C': ['E'], 'D': ['F'], 'E': ['H', 'F'], 'F': ['G'], 'G': [], 'H': []}
print(topological_sort(example_graph))  # ['A', 'B', 'C', 'D', 'E', 'H', 'F', 'G']
