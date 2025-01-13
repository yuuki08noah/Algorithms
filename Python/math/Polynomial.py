class Polynomial:
    def __init__(self, polynomial):
        self.polynomial = polynomial

    def __add__(self, other):
        res = Polynomial({i:0 for i in range(max(max(self.polynomial.keys()), max(other.polynomial.keys())))})
        for i in range(max(max(self.polynomial.keys()), max(other.polynomial.keys())), -1, -1):
            if i not in self.polynomial and i not in other.polynomial:
                continue
            if i not in self.polynomial:
                res.polynomial[i] = other.polynomial[i]
            elif i not in other.polynomial:
                res.polynomial[i] = self.polynomial[i]
            else:
                res.polynomial[i] = other.polynomial[i] + self.polynomial[i]
        return res

    def __sub__(self, other):
        res = Polynomial({i:0 for i in range(max(max(self.polynomial.keys()), max(other.polynomial.keys())))})
        if max(other.polynomial.keys()) > max(self.polynomial.keys()):
            for i in range(max(other.polynomial.keys()), max(self.polynomial.keys()), -1):
                if i not in other.polynomial:
                    continue
                res.polynomial[i] = -other.polynomial[i]
        for i in range(max(self.polynomial.keys()), -1, -1):
            if i not in self.polynomial and i not in other.polynomial:
                continue
            if i not in other.polynomial:
                res.polynomial[i] = self.polynomial[i]
            else:
                res.polynomial[i] = self.polynomial[i] - other.polynomial[i]
        return res

    def __mul__(self, other):
        res = Polynomial({i: 0 for i in range(max(self.polynomial)+max(other.polynomial)+1)})
        for i in self.polynomial.keys():
            for j in other.polynomial.keys():
                if self.polynomial[i] == 0 or other.polynomial[j] == 0:
                    continue
                res.polynomial[i+j] += self.polynomial[i]*other.polynomial[j]
        return res

    def __repr__(self):
        r = ''
        try:
            while self.polynomial[max(self.polynomial.keys())] == 0:
                del self.polynomial[max(self.polynomial.keys())]
        except:
            return '0'

        for i in range(max(self.polynomial.keys()), -1, -1):
            if i not in self.polynomial or self.polynomial[i] == 0: continue
            if i != max(self.polynomial.keys()):
                if self.polynomial[i] > 0:
                    r += '+'
            if i == 0: r += str(self.polynomial[i])
            else: r += str(self.polynomial[i]) + f'x^{i}'
        return r
