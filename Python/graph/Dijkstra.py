import heapq

class Dijkstra:
    def __init__(self, table, start):
        self.table = table
        self.start = start
        self.length = len(table)
        self.costs = [10**9] * self.length

    def dijkstra(self):
        self.costs[self.start - 1] = 0  # 시작 노드 0

        queue = [(0, self.start)]

        while queue:  # dijkstra
            cost, node = heapq.heappop(queue)

            if cost > self.costs[node - 1]:  # 만약 노드 비용이 현재 비용보다 더 크다면
                continue

            if node in self.table:
                for weight, next_node in self.table[node]:
                    if weight + cost < self.costs[next_node - 1]:  # 더 작은 값일 경우 queue 에 넣고 배열 수정
                        self.costs[next_node - 1] = weight + cost
                        heapq.heappush(queue, (self.costs[next_node - 1], next_node))

        return self.costs[:]