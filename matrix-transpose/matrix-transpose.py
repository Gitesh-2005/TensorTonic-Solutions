import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    rows = len(A)
    cols = len(A[0])

    T = np.zeros((cols, rows))

    for i in range(rows):
        for j in range(cols):
            T[j][i] = A[i][j]

    return T