from Python.math.Matrix import Matrix
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m = Matrix(A)
print(m.determinant())