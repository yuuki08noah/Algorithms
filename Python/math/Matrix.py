from Python.Exceptions.MatrixShapeMismatchException import MatrixShapeMismatchException

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str(self.matrix)
    def __repr__(self):
        return str(self.matrix)

    def __mul__(self, other):
        if len(other.matrix) != len(self.matrix[0]):
            raise MatrixShapeMismatchException()
        res_matrix = Matrix([0 for _ in range(len(other.matrix[0]))])
        for i in range(len(self.matrix)):
            temp = [0] * len(other.matrix[0])
            for j in range(len(other.matrix[0])):
                value = 0
                for k in range(len(other.matrix)):
                    value += self.matrix[i][k] * other.matrix[k][j]
                temp[j] = value
            res_matrix.matrix[i] = temp
        return res_matrix

    def __add__(self, other):
        if len(other.matrix) != len(self.matrix) or len(other.matrix[0]) != len(self.matrix[0]):
            raise MatrixShapeMismatchException()
        res_matrix = Matrix([0 for _ in range(len(other.matrix[0]))] * len(self.matrix))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res_matrix.matrix[i][j] = other.matrix[i][j] + res_matrix[i][j]
        return res_matrix

    def __pow__(self, exp):
        if len(self.matrix) != len(self.matrix[0]):
            raise MatrixShapeMismatchException()
        if exp == 1:
            return self
        elif exp % 2 == 0:
            temp = self ** (exp // 2)
            return temp * temp
        else:
            temp = self ** (exp // 2)
            return self * temp * temp

