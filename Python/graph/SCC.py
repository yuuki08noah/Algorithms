class SCC:
    def __init__(self, graph, inversed_graph):
        self.graph = graph
        self.inversed_graph = inversed_graph
        self.size = max(graph)
        self.visited = [False] * (self.size + 1)
        self.inversed_visited = [False] * (self.size + 1)
        self.sequence = 0
        self.order = {}

    def kosaraju(self):
        for i in range(1, self.size + 1):
            if not self.visited[i]:
                self.visited[i] = True
                self.dfs(i, 1)

        scc = []
        for key, value in sorted(self.order.items(), reverse=True, key=lambda item: item[0]):
            if not self.inversed_visited[value]:
                self.inversed_visited[value] = True
                li = []
                self.dfs(value, 2, li)
                scc.append(li)
        return scc

    def dfs(self, n, step, li=None):
        if step == 1:
            for node in self.graph[n]:
                if not self.visited[node]:
                    self.visited[node] = True
                    self.dfs(node, step)
            self.order[self.sequence] = n
            self.sequence += 1
        else:
            li.append(n)
            for node in self.inversed_graph[n]:
                if not self.inversed_visited[node]:
                    self.inversed_visited[node] = True
                    self.dfs(node, step, li)