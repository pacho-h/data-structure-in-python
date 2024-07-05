def find_connected_components(graph):
    visited = set()
    components = []

    def dfs(v):
        stack = [v]
        component = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                component.append(vertex)
                stack.extend([neighbor for neighbor in graph[vertex] if neighbor not in visited])
        return component

    for vertex in graph:
        if vertex not in visited:
            components.append(dfs(vertex))
    return components


# 사용 예제
graph_disconnected = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
print(find_connected_components(graph_disconnected))  # [['A', 'B'], ['C', 'D'], ['E']]
