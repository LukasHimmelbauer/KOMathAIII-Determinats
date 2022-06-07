import numpy as np


# recursively called function to calculate determinant from always smaller mats
def calc_laplace_determinant(mat: np.array):
    # if matrix is just 1x1 then just return value
    if mat.shape == (1, 1):
        return mat[0][0]

    sum = 0
    for i in range(0, mat.shape[0]):
        pm = (-1) ** i
        val = mat[i, 0]

        new = np.delete(mat, i, 0)
        new = np.delete(new, 0, 1)

        sum += pm * val * calc_laplace_determinant(new)

    return sum
