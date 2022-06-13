import numpy as np

# Press the green button in the gutter to run the script.
from gauss import gauss_determinant
from laplace import calc_laplace_determinant
from lu_decomposition import lu_decomposition_determinant

if __name__ == '__main__':
    print(calc_laplace_determinant(np.array([
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
    ],dtype=float)))

    print(lu_decomposition_determinant(np.array([
        [1, 2, 3, 4],
        [5, 6, 1, 8],
        [9, 1, 2, 3],
        [4, 5, 6, 7]
    ], dtype=float)))