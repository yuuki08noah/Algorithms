import math

class TaylorSeries:
    factorial = [1] * 31
    pi = math.pi

    def __init__(self):
        for i in range(1, 31):
            self.factorial[i] = i * self.factorial[i - 1]

    def exponential(self, x):
        res = 0
        for i in range(0, 31):
            res += pow(x, i) / self.factorial[i]
        return res

    def sin(self, x):
        res = 0
        for i in range(0, 15):
            res += pow(-1, i) * pow(x, 2*i+1) / self.factorial[2*i+1]
        return res

    def cos(self, x):
        res = 0
        for i in range(0, 15):
            res += pow(-1, i) * pow(x, 2*i) / self.factorial[2*i]
        return res