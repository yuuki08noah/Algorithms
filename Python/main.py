from Python.graph.SCC import SCC

v, e = map(int, input().split())
graph = {i:[] for i in range(1, v + 1)}
graph_inversed = {i:[] for i in range(1, v + 1)}
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph_inversed[b].append(a)

SCC = SCC(graph, graph_inversed)
print(SCC.kosaraju())