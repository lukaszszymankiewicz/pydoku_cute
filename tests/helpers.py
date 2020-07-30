import numpy as np


def sudoku_is_valid(array: np.ndarray) -> bool:
    sorted_sudoku = np.sort(array, axis=1)
    for row in sorted_sudoku:
        if np.any(row != np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])):
            return False

    sorted_sudoku = np.sort(array, axis=0)
    for cols in sorted_sudoku.T:
        if np.any(row != np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])):
            return False

    return True
