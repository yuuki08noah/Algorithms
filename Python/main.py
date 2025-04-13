from Python.math.Matrix import Matrix
A = [
    [1, 2, 3, 4, 5],
    [4, 5, 6 ,4, 3],
    [7, 8, 9, 2, 2],
    [1, 2, 4, 6, 3],
    [2, 2, 5, 6, 3]
]
m = Matrix(A)
print(m.adjoint())