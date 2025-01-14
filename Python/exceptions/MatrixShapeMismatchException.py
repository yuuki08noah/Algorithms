class MatrixShapeMismatchException(Exception):
    def __init__(self, message="Matrix shape mismatch"):
        self.message = message
    def __str__(self):
        return self.message