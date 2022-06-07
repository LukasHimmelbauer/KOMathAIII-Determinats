# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

# Press the green button in the gutter to run the script.
from gauss import gauss_determinant
from laplace import calc_laplace_determinant

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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
