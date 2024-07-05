import heapq


def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]

    while min_heap:
        weight, current, prev = heapq.heappop(min_heap)
        if current not in visited:
            visited.add(current)
            if prev is not None:
                mst.append((prev, current, weight))
            for neighbor, weight in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, current))

    return mst


# 사용 예제
example_graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 3), ('D', 6)],
    'C': [('A', 3), ('B', 3), ('D', 4)],
    'D': [('B', 6), ('C', 4)],
}

# 사용 예제
print(prim(example_graph, 'A'))  # [('A', 'B', 1), ('A', 'C', 3), ('C', 'D', 4)]
