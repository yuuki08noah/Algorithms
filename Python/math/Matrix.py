from Python.exceptions.DeterminantZeroException import DeterminantZeroException
from Python.exceptions.MatrixShapeMismatchException import MatrixShapeMismatchException

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        return str(self.matrix)
    def __repr__(self):
        return str(self.matrix)

    def __mul__(self, other):
        if other.rows != self.cols:
            raise MatrixShapeMismatchException()
        res_matrix = []
        for i in range(self.rows):
            temp = [0] * other.cols
            for j in range(other.cols):
                value = 0
                for k in range(other.rows):
                    value += self.matrix[i][k] * other.matrix[k][j]
                temp[j] = value
            res_matrix.append(temp)
        return Matrix(res_matrix)

    def __add__(self, other):
        if other.rows != self.rows or other.cols != other.cols:
            raise MatrixShapeMismatchException()
        res_matrix = Matrix([0 for _ in range(other.cols)] * self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                res_matrix.matrix[i][j] = other.matrix[i][j] + res_matrix[i][j]
        return res_matrix

    def __pow__(self, exp):
        if self.rows != self.cols:
            raise MatrixShapeMismatchException()

        if exp == -1:
            if self.determinant() == 0:
                raise DeterminantZeroException("Determinant cannot be zero")
            return self.adjoint().scalar_multiplication(1/self.determinant())

        elif exp == 1:
            return self
        elif exp % 2 == 0:
            temp = self ** (exp // 2)
            return temp * temp
        else:
            temp = self ** (exp // 2)
            return self * temp * temp

    def transpose(self, matrix):
        transposed = list(map(list, zip(*matrix)))
        return Matrix(transposed)

    def scala_multiplication(self, x, matrix):
        new_matrix = []
        for i in range(matrix.rows):
            temp = []
            for j in range(matrix.cols):
                temp.append(x * matrix.matrix[i][j])
            new_matrix.append(temp)
        return Matrix(new_matrix)

    def determinant(self, matrix):
        if matrix.rows == 1:
            return matrix.matrix[0][0]
        elif matrix.rows == 2:
            return matrix.matrix[0][0] * matrix.matrix[1][1] - matrix.matrix[0][1] * matrix.matrix[1][0]
        else:
            temp = 0
            for j in range(matrix.cols):
                temp += (-1) ** j * matrix.matrix[0][j] * self.determinant(self.cofactor(matrix, 0, j))
            return temp

    def cofactor(self, matrix, x, y):
        new_matrix = []
        for i in range(matrix.rows):
            temp = []
            if i == x: continue
            for j in range(matrix.cols):
                if j == y: continue
                temp.append(matrix.matrix[i][j])
            new_matrix.append(temp)
        return Matrix(new_matrix)

    def adjoint(self, matrix):
        new_matrix = []
        for i in range(matrix.rows):
            temp = []
            for j in range(matrix.cols):
                temp.append((-1) ** (i + j) * self.determinant(self.cofactor(matrix, i, j)))
            new_matrix.append(temp)

        return self.transpose(Matrix(new_matrix))
