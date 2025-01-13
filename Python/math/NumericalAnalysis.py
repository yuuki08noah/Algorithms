import math
from decimal import Decimal

class NumericalAnalysis:
    def __init__(self, equation):
        self.function = equation

    def bisection_method(self):
        start, end = Decimal(-10 ** 10), Decimal(10 ** 10)  # 시작 범위
        for _ in range(1000):
            mid = (start + end) / Decimal(2.0)
            if self.function(mid) < 0:
                start = mid
            else:
                end = mid
        return mid

    def newtons_method(self, init, derivative):
        x = Decimal(init)
        for _ in range(1000):
            x = x - self.function(x) / derivative(x)
        return x