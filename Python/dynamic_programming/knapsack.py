class Knapsack:
    def __init__(self, items, capacity, weights, values):
        self.capacity = capacity
        self.dp = [0] * (capacity+1)
        self.items = items
        self.weights = weights
        self.values = values

    def solve(self):
        for i in range(self.items):
            for j in range(self.capacity, self.weights[i]-1, -1):
                self.dp[j] = max(self.dp[j], self.dp[j-self.weights[i]]+self.values[i])
        return max(self.dp)

knapsack = Knapsack(4, 7, [6, 4, 3, 5], [13, 8, 6, 12])
print(knapsack.solve())