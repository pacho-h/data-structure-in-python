class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1


def kruskal(graph):
    edges = []
    for v in graph:
        for u, weight in graph[v]:
            edges.append((weight, v, u))
    edges.sort()

    vertices = graph.keys()
    ds = DisjointSet(vertices)
    mst = []

    for weight, v, u in edges:
        if ds.find(v) != ds.find(u):
            ds.union(v, u)
            mst.append((v, u, weight))

    return mst


# 사용 예제
example_graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 3), ('D', 6)],
    'C': [('A', 3), ('B', 3), ('D', 4)],
    'D': [('B', 6), ('C', 4)],
}
print(kruskal(example_graph))  # [('A', 'B', 1), ('A', 'C', 3), ('C', 'D', 4)]
