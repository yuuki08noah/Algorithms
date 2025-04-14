from Python.graph.Dijkstra import Dijkstra

graph = {
    1: [(20, 2), (13, 4), (6, 7)],
    2: [(6, 5), (12, 4)],
    3: [(7, 2), (14, 5)],
    4: [(9, 7), (10, 5)],
    5: [],
    6: [(11, 3)],
    7: [(10, 6)]
}

A = Dijkstra(graph, 1)
print(A.dijkstra())
