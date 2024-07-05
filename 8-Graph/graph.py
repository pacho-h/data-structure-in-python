class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v, w):
        if v in self.graph and w in self.graph:
            self.graph[v].append(w)
            self.graph[w].append(v)  # 무향 그래프의 경우

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for v in self.graph:
            for w in self.graph[v]:
                if {v, w} not in edges:
                    edges.append({v, w})
        return edges


# 사용 예제
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge('A', 'B')
g.add_edge('B', 'C')
print(g.get_vertices())  # ['A', 'B', 'C']
print(g.get_edges())  # [{'A', 'B'}, {'B', 'C'}]
