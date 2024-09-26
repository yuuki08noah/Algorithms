from collections import deque
class DFS:
    def __init__(self, table):
        self.len = len(table)
        self.table = table
        self.visited = [False] * (self.len + 1)
        self.result = []

    def refresh(self):
        self.visited = [False] * (self.len + 1)
        self.result = []

    def BFS(self, node):
        self.result.append(node)
        self.visited[node] = True
        queue = deque([node])
        while queue:
            node = queue.popleft()
            self.result.append(node)
            self.visited[node] = True
            for vertex in self.table[node]:
                if not self.visited[vertex]:
                    queue.append(vertex)