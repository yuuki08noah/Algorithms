from Python.math.Matrix import Matrix
A = [
    [2, 1, 0, 3, 4],
    [1, 2, 1, 1, 0],
    [3, 0, 2, 4, 1],
    [0, 1, 3, 2, 5],
    [4, 2, 1, 0, 3]
]
m = Matrix(A)
print((m**-1)*m)