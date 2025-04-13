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
        res_matrix = Matrix([0 for _ in range(other.cols)])
        for i in range(self.rows):
            temp = [0] * other.cols
            for j in range(other.cols):
                value = 0
                for k in range(other.rows):
                    value += self.matrix[i][k] * other.matrix[k][j]
                temp[j] = value
            res_matrix.matrix[i] = temp
        return res_matrix

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

        if exp == 1:
            return self
        elif exp % 2 == 0:
            temp = self ** (exp // 2)
            return temp * temp
        else:
            temp = self ** (exp // 2)
            return self * temp * temp

    def adjoint(self):
        res = []
        for i in range(self.rows):
            temp = []
            for j in range(self.cols):
                temp.append(((-1)**(i+j))*self.determinant(self.cofactor(None, i, j)))
            res.append(temp)
        return self.transpose(res)

    def transpose(self, matrix):
        transposed = list(map(list, zip(*matrix)))
        return Matrix(transposed)

    def determinant(self, matrix=None):
        if matrix is None:
            matrix = self.matrix
        if len(matrix) != len(matrix[0]):
            raise MatrixShapeMismatchException()
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            res = 0
            for j in range(len(matrix[0])):
                res += matrix[0][j]*((-1)**(0+j))*self.determinant(self.cofactor(matrix, 0, j))
            return res

    def cofactor(self, matrix, i, j):
        if matrix is None:
            matrix = self.matrix
        temp = []
        for k in range(len(matrix)):
            if k == i: continue
            row = []
            for l in range(len(matrix[0])):
                if l == j: continue
                row += [matrix[k % len(matrix)][l % len(matrix[0])]]
            temp.append(row)
        return temp