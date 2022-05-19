# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


# recursively called function to calculate determinant from always smaller mats
def calcLaplaceDeterminant(mat: np.array):
    # if matrix is just 1x1 then just return value
    if mat.shape == (1, 1):
        return mat[0][0]

    sum = 0
    for i in range(0, mat.shape[0]):
        pm = (-1) ** i
        val = mat[i, 0]

        new = np.delete(mat, i, 0)
        new = np.delete(new, 0, 1)

        sum += pm * val * calcLaplaceDeterminant(new)

    return sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calcLaplaceDeterminant(np.array([
        [1, 2, 3, 4],
        [5, 6, 1, 8],
        [9, 1, 2, 3],
        [4, 5, 6, 7]
    ])))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
