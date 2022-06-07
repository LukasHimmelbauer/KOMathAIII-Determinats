import numpy as np


def gauss_elimination(mat: np.array):
    for i in range(mat.shape[0]-1):
        for ii in range(i+1, mat.shape[0]):
            mat[ii] = mat[ii] - mat[ii, i]/mat[i, i]*mat[i]
    return mat


def gauss_determinant(mat: np.array):
    return gauss_elimination(mat).diagonal().prod()


if __name__ == "__main__":
    print(gauss_determinant(np.array([[1, 5, 3], [2, 8, 4], [9, 7, 1]], dtype=float)))
    print(gauss_elimination(np.array([
        [1, 2, 3, 4],
        [5, 6, 1, 8],
        [9, 1, 2, 3],
        [4, 5, 6, 7]
    ])))
    print(gauss_determinant(np.array([
        [1, 2, 3, 4],
        [5, 6, 1, 8],
        [9, 1, 2, 3],
        [4, 5, 6, 7]
    ], dtype=float)))
