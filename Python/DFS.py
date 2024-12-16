class DFS:
    def __init__(self, table):
        self.len = len(table)
        self.table = table
        self.visited = [False] * (self.len + 1)
        self.result = []

    def refresh(self):
        self.visited = [False] * (self.len + 1)
        self.result = []

    def recursiveDFS(self, node):
        self.result.append(node)
        self.visited[node] = True
        for vertex in self.table[node]:
            if not self.visited[vertex]:
                self.recursiveDFS(vertex)

    def repeatDFS(self, startNode):
        stack = [startNode]
        while stack:
            node = stack.pop()
            self.result.append(node)
            self.visited[node] = True
            for i in self.table[node]:
                if not self.visited[i]:
                    stack.append(i)